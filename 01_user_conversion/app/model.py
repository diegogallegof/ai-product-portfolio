from pathlib import Path

import joblib
import pandas as pd

from .schemas import UserSignals


MODEL_PATH = (
    Path(__file__)
    .resolve()
    .parents[1]
    / "models"
    / "baseline_logreg_pipeline.joblib"
)


class ConversionScoringModel:
    """
    Lightweight wrapper around the persisted baseline conversion model.

    Responsibilities:
    - Load the trained scikit-learn pipeline
    - Accept structured user signals
    - Return conversion probability

    This class is intentionally minimal and stateless after initialization.
    """

    def __init__(self):
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                f"Model artifact not found at expected path: {MODEL_PATH}"
            )

        self.model = joblib.load(MODEL_PATH)

        # Optional but highly recommended: keep a canonical feature list
        # for clearer errors when wiring the API.
        self.expected_features = [
            "days_since_signup",
            "sessions_7d",
            "content_hours_7d",
            "downloads_7d",
            "paywall_views_7d",
            "country_tier",
        ]

    @staticmethod
    def to_dataframe(signals: UserSignals) -> pd.DataFrame:
        return pd.DataFrame([signals.model_dump()])

    def score(self, input_df: pd.DataFrame) -> float:
        """
        Score a single user snapshot.

        Parameters
        ----------
        input_df : pd.DataFrame
            DataFrame with a single row containing the same feature schema used during training.

        Returns
        -------
        float
            Probability of subscription conversion.
        """
        if input_df.shape[0] != 1:
            raise ValueError("Input DataFrame must contain exactly one row.")

        # Validate schema (clear errors > cryptic sklearn errors)
        missing = [c for c in self.expected_features if c not in input_df.columns]
        extra = [c for c in input_df.columns if c not in self.expected_features]
        if missing:
            raise ValueError(f"Missing required features: {missing}")
        if extra:
            raise ValueError(f"Unexpected extra features: {extra}")

        # Ensure column order is stable
        input_df = input_df[self.expected_features]

        proba = self.model.predict_proba(input_df)[0, 1]
        return float(proba)
