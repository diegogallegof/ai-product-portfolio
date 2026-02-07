from pathlib import Path
import joblib
import pandas as pd


# Resolve model path relative to this file
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

    def score(self, input_df: pd.DataFrame) -> float:
        """
        Score a single user snapshot.

        Parameters
        ----------
        input_df : pd.DataFrame
            DataFrame with a single row containing the same feature
            schema used during training.

        Returns
        -------
        float
            Probability of subscription conversion.
        """
        if input_df.shape[0] != 1:
            raise ValueError("Input DataFrame must contain exactly one row.")

        proba = self.model.predict_proba(input_df)[0, 1]
        return float(proba)
