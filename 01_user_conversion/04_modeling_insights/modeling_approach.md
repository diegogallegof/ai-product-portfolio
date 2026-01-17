# Modeling Approach

This document explains the modeling approach used in this case study and why it is intentionally
biased toward **interpretability and decision usefulness** over maximum predictive performance.

The goal is to answer: **What behaviors matter for conversion, and what should product do about it?**

---

## 1) Why we model at all

Modeling is used as a structured way to:

- Compare signals under a consistent framework
- Quantify relative importance and directionality
- Identify redundancy between signals
- Stress-test intuition against data
- Produce insights that can guide experiments and prioritization

In this case study, a model is a **compression tool**:
it summarizes many behaviors into a small set of interpretable explanations.

---

## 2) Decision-oriented modeling principles

All models used in this phase must satisfy these principles:

1. **Interpretability first**
   - A product stakeholder should understand *why* the model suggests an outcome.

2. **Simplicity wins by default**
   - If a simple model performs similarly to a complex one, the simple model is preferred.

3. **Temporal integrity**
   - Training and validation must respect time. Random splits can produce false confidence.

4. **Robustness over optimization**
   - We prioritize stability across cohorts over squeezing marginal performance.

5. **Actionability**
   - Model insights must map back to signals and product levers.

---

## 3) Model ladder (from simplest to more complex)

We follow a progressive “model ladder”.
We only move upward if it adds clear insight.

### 3.1 Baseline heuristics (non-ML)
Purpose: establish a decision baseline.

Examples:
- Segment rules (e.g., high intent if premium page visited + high engagement)
- Simple thresholds (e.g., activation achieved within D1)

Why: if heuristics perform close to ML, ML may not be necessary for decisioning.

---

### 3.2 Logistic regression (interpretable baseline)
Purpose: quantify direction and magnitude with clear coefficients.

Use cases:
- Identify which signals are strongly associated with conversion
- Estimate incremental effects while controlling for other signals

Interpretation:
- Coefficients map naturally to “which signals push conversion up or down”

---

### 3.3 Shallow decision trees (human-readable rules)
Purpose: produce “if/then” logic aligned with product segmentation.

Use cases:
- Discover interaction effects (e.g., intent matters only after activation)
- Generate segment definitions for experimentation

Constraint:
- Keep depth small to preserve interpretability.

---

### 3.4 (Optional) Simple ensemble models
Only considered if:
- They provide a meaningful insight gap vs interpretable models
- They can be explained via feature importance and stability checks
- They do not become black-box artifacts

Examples:
- Random forest with strict interpretability guardrails
- Gradient boosting only if paired with explainability and stability tests

---

## 4) Training and validation strategy

### 4.1 Time-based splits
We use time-based splits to avoid “future leakage”.

Rationale:
- Conversion behavior shifts over time (seasonality, campaigns, product changes)
- Random splits overestimate generalization

Approach:
- Train on earlier cohorts, validate on later cohorts
- Repeat across multiple time windows if possible

---

### 4.2 Cohort robustness checks
Models must be checked across:
- Acquisition source cohorts
- Geography cohorts (if applicable)
- Platform cohorts (if applicable)

A model that only works in one slice is not suitable for broad product decisioning.

---

### 4.3 Evaluation metrics (decision-focused)
Primary:
- AUC / ROC as a general discriminative signal (not the goal)
- Precision/recall at operational thresholds (for targeting decisions)

Secondary:
- Stability of feature importance across cohorts
- Calibration sanity checks (do predicted probabilities behave sensibly?)

We do not optimize for a single metric.
We optimize for **consistent decision guidance**.

---

## 5) How we extract insights (not just predictions)

Model outputs are translated into product insights via:

- Feature importance and coefficient direction
- Segment discovery (tree rules)
- Interaction analysis (when signals matter conditional on others)
- “Earliest reliable window” analysis (D1 vs D7 trade-offs)

The output is not “a score” — it is a set of **explanations** and **recommendations**.

---

## 6) What we deliberately avoid

- Hyperparameter tuning as a goal
- Deep learning or opaque architectures
- Models that cannot be explained to stakeholders
- “Leaderboard thinking” (accuracy without decisions)

---

## 7) Output of this document

This approach defines:
- Which models are acceptable in this case study
- How they will be validated
- How results will be interpreted for product action

This provides the foundation for:
- `feature_set_definition.md`
- `baseline_models.md`
- `insight_extraction.md`
