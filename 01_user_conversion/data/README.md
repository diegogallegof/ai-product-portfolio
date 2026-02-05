# Synthetic User Conversion Data — Data Contract

This folder contains the **synthetic dataset** used in the *User Conversion Case Study*.

The goal of this data is **not realism at the raw-data level**, but **realism at the behavioral and decision level**:
signals are designed to mirror how a subscription-based streaming product reasons about user conversion.

This document defines the **data contract**: what each feature represents, its expected behavior, and how the target label is generated.

---

## 🎯 Dataset purpose

The dataset is designed to support:

- Exploratory analysis oriented toward modeling
- Training an **interpretable baseline conversion model**
- Demonstrating how product signals translate into decision-support systems

It intentionally avoids:
- User-level PII
- Overly complex feature engineering
- Perfect separability between converters and non-converters

---

## 📂 Files in this folder

- `synthetic_data.py`  
  Python script that **generates the dataset** deterministically.

- `synthetic_user_conversion_data.csv`  
  Generated dataset used by notebooks and models.  
  This file is **overwritten** each time the generator is executed.

---

## 🔁 Reproducibility

- The dataset is generated with a fixed random seed.
- Running `synthetic_data.py` multiple times produces **identical data** unless:
  - the random seed is changed
  - feature distributions or weights are modified

This allows controlled experimentation on modeling choices.

---

## 🧠 Feature definitions

Each row represents a **single user snapshot**.

### `days_since_signup`
- Type: integer
- Description: Number of days since the user created their account
- Range: positive integers
- Product meaning: Lifecycle stage / user maturity

---

### `sessions_7d`
- Type: integer
- Description: Number of app sessions in the last 7 days
- Product meaning: Engagement frequency

---

### `content_hours_7d`
- Type: float
- Description: Total hours of content consumed in the last 7 days
- Product meaning: Depth of engagement

---

### `downloads_7d`
- Type: integer
- Description: Number of content downloads in the last 7 days
- Product meaning: Offline intent / commitment signal

---

### `paywall_views_7d`
- Type: integer
- Description: Number of paywall impressions in the last 7 days
- Product meaning: Exposure to monetization moments

---

### `country_tier`
- Type: categorical (`tier_1`, `tier_2`, `tier_3`)
- Description: Market-level abstraction of country economics
- Product meaning: Purchasing power and pricing context

---

## 🎯 Target variable

### `converted`
- Type: binary (`0` / `1`)
- Description: Whether the user converted to a paid subscription
- Generation logic:
  - Probability of conversion is computed using a **logistic function**
  - Inputs include behavioral signals and country tier effects
  - Random noise is added to avoid deterministic outcomes

This ensures:
- Partial overlap between converters and non-converters
- Realistic uncertainty similar to production systems

---

## ⚖️ Design principles and limitations

- The data is **signal-driven**, not event-log driven
- Feature correlations are intentional but not extreme
- The dataset favors **interpretability over realism at scale**
- Absolute performance metrics are not the objective

The dataset is designed to answer:
> “Given realistic behavioral signals, how would a product team reason about conversion probability?”

---

## 🧩 Downstream usage

This dataset feeds directly into:

1. Exploratory data analysis (EDA)
2. Baseline model training (Logistic Regression)
3. Model artifact generation (`.joblib`)
4. Conversion scoring API (next phase)

It acts as the **foundation** of the end-to-end case study.
