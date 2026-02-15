from fastapi import FastAPI
from fastapi.responses import JSONResponse

from .decision import ConversionDecisionEngine
from .model import ConversionScoringModel
from .schemas import ScoreResponse, UserSignals

app = FastAPI(
    title="User Conversion Scoring API",
    version="0.2.0",
    description="Decision-support scoring service for the baseline conversion model.",
)

# Load model once on startup (avoid loading per-request)
model = ConversionScoringModel()

# Decision layer (policy) lives outside the model
decision_engine = ConversionDecisionEngine()

MODEL_VERSION = "baseline_logreg_pipeline.joblib"


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": True, "model_version": MODEL_VERSION}


@app.post("/score", response_model=ScoreResponse)
def score(signals: UserSignals):
    try:
        input_df = model.to_dataframe(signals)
        proba = model.score(input_df)
        segment = decision_engine.decide(proba)

        return ScoreResponse(
            conversion_probability=proba,
            decision_segment=segment,
            model_version=MODEL_VERSION,
        )
    except ValueError as e:
        # Input validation / schema issues
        return JSONResponse(status_code=400, content={"error": str(e)})
    except Exception:
        # Unexpected failures
        return JSONResponse(status_code=500, content={"error": "Internal server error"})
