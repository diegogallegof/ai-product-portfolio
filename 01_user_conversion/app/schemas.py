from enum import Enum
from pydantic import BaseModel, Field, ConfigDict


class CountryTier(str, Enum):
    tier_1 = "tier_1"
    tier_2 = "tier_2"
    tier_3 = "tier_3"


class UserSignals(BaseModel):
    """
    Input schema for conversion scoring.

    This must match the feature schema used during model training.
    """

    model_config = ConfigDict(extra="forbid")  # reject unknown fields

    days_since_signup: int = Field(..., ge=0, description="Days since user signup")
    sessions_7d: int = Field(..., ge=0, description="App sessions in the last 7 days")
    content_hours_7d: float = Field(..., ge=0, description="Content hours consumed in the last 7 days")
    downloads_7d: int = Field(..., ge=0, description="Downloads in the last 7 days")
    paywall_views_7d: int = Field(..., ge=0, description="Paywall impressions in the last 7 days")
    country_tier: CountryTier = Field(..., description="Market purchasing power tier")


class ScoreResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    conversion_probability: float = Field(..., ge=0.0, le=1.0, description="Predicted probability of conversion")
    model_version: str = Field(..., description="Model artifact version identifier")
