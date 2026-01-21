import numpy as np
import pandas as pd

RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)


def generate_synthetic_users(n_users: int = 5000) -> pd.DataFrame:
    """
    Generate synthetic user-level behavioral data for a subscription product.
    """

    # Lifecycle
    days_since_signup = np.random.randint(1, 60, size=n_users)

    # Engagement signals (early-heavy distribution)
    sessions_7d = np.random.poisson(lam=3, size=n_users)
    content_hours_7d = np.round(
        np.random.gamma(shape=2, scale=1.5, size=n_users), 2
    )
    downloads_7d = np.random.poisson(lam=1, size=n_users)
    paywall_views_7d = np.random.poisson(lam=1.2, size=n_users)

    # Geography / purchasing power
    country_tier = np.random.choice(
        ["Tier_1", "Tier_2", "Tier_3"],
        size=n_users,
        p=[0.35, 0.40, 0.25],
    )

    df = pd.DataFrame(
        {
            "days_since_signup": days_since_signup,
            "sessions_7d": sessions_7d,
            "content_hours_7d": content_hours_7d,
            "downloads_7d": downloads_7d,
            "paywall_views_7d": paywall_views_7d,
            "country_tier": country_tier,
        }
    )

    return df


def generate_conversion_label(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate a probabilistic conversion label based on behavioral signals.
    """

    score = (
        0.30 * df["sessions_7d"]
        + 0.50 * df["downloads_7d"]
        + 0.40 * df["paywall_views_7d"]
        + 0.25 * df["content_hours_7d"]
        - 0.02 * df["days_since_signup"]
    )

    # Country effect
    country_effect = df["country_tier"].map(
        {"Tier_1": 0.8, "Tier_2": 0.3, "Tier_3": -0.2}
    )
    score += country_effect

    # Noise (real life is messy)
    noise = np.random.normal(0, 0.8, size=len(df))
    score += noise

    # Logistic transformation
    probability = 1 / (1 + np.exp(-score))

    df["converted"] = np.random.binomial(1, probability)

    return df


if __name__ == "__main__":
    df = generate_synthetic_users(n_users=5000)
    df = generate_conversion_label(df)

    print(df.head())
    print("\nConversion rate:", df["converted"].mean())

    df.to_csv("synthetic_user_conversion_data.csv", index=False)
    print("\nSaved synthetic_user_conversion_data.csv")
