from fastapi import FastAPI
from fastapi.responses import JSONResponse

from .model import ConversionScoringModel
from .schemas import UserSignals, ScoreResponse

app = FastAPI(
    title="User Conversion Scoring API",
    version="0.1.0",
    description="Minimal scoring service for the baseline conversion model (decision-support).",
)

# Load model once on startup (avoid loading per-request)
model = ConversionScoringModel()

MODEL_VERSION = "baseline_logreg_pipeline.joblib"


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": True, "model_version": MODEL_VERSION}


@app.post("/score", response_model=ScoreResponse)
def score(signals: UserSignals):
    try:
        input_df = model.to_dataframe(signals)
        proba = model.score(input_df)
        return ScoreResponse(
            conversion_probability=proba,
            model_version=MODEL_VERSION,
        )
    except ValueError as e:
        # Input validation / schema issues
        return JSONResponse(status_code=400, content={"error": str(e)})
    except Exception as e:
        # Unexpected failures
        return JSONResponse(status_code=500, content={"error": "Internal server error"})
