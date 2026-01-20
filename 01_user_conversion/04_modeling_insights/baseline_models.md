# Baseline Models

This document defines the baseline models used to evaluate
how much explanatory and decision value can be obtained
from **simple, interpretable approaches**.

Baseline models serve as **reference points**.
If complex models do not meaningfully outperform these baselines,
they are not justified for product decisioning.

---

## 1) Purpose of baseline models

Baseline models are used to:

- Establish a minimum performance benchmark
- Test whether signals add value beyond intuition
- Validate that modeling effort is justified
- Preserve interpretability for stakeholders

The goal is **not** to achieve the highest possible accuracy,
but to understand **what can be explained with the simplest tools**.

---

## 2) Baseline hierarchy

Models are evaluated in increasing order of complexity.
We only move forward if additional complexity provides clear insight.

---

## 3) Baseline 0: Naive heuristics (non-ML)

### Description
Rule-based heuristics derived directly from product intuition.

Examples:
- User is high-intent if `premium_page_visit = 1`
- User is likely to convert if `activated_d1 = 1` AND `core_actions_7d ≥ threshold`

### Purpose
- Establish a human-readable decision baseline
- Set expectations for model performance
- Identify whether ML adds incremental value

### Evaluation
- Conversion lift vs global baseline
- Precision at simple operational thresholds

If heuristics perform close to ML models,
they may be preferred for simplicity and explainability.

---

## 4) Baseline 1: Single-signal models

### Description
Models using **one feature at a time**
to evaluate isolated signal strength.

Typical approach:
- Logistic regression with a single feature
- Univariate decision tree splits

### Purpose
- Quantify the standalone impact of each signal
- Detect weak or redundant signals
- Validate assumptions from Phase 3

### Evaluation
- AUC vs naive baseline
- Direction and magnitude of effect
- Stability across cohorts

Signals that fail at this stage are excluded from further modeling.

---

## 5) Baseline 2: Multi-signal interpretable models

### Description
Simple multivariate models combining a small set of features.

Typical models:
- Logistic regression
- Shallow decision trees (limited depth)

### Purpose
- Measure incremental value of combining signals
- Identify interactions between behaviors
- Control for confounding effects

### Evaluation
- Incremental AUC vs single-signal models
- Feature coefficient stability
- Interpretability of interactions

Models are kept intentionally small to preserve clarity.

---

## 6) Model evaluation criteria

Baseline models are evaluated using:

- **Discrimination**
  - AUC / ROC as a general signal
- **Decision utility**
  - Precision / recall at actionable thresholds
- **Stability**
  - Consistency across time-based splits
- **Interpretability**
  - Ability to explain outcomes to stakeholders

No single metric determines success.
Models must perform **consistently and understandably**.

---

## 7) What success looks like

Baseline modeling is considered successful if:

- A small number of signals explain a meaningful share of behavior
- Simple models approach the performance of more complex ones
- Trade-offs between early and late prediction are clear
- Product-relevant insights emerge without black-box methods

If these conditions are met,
additional complexity is not required.

---

## 8) Relationship to next steps

Outputs from baseline models feed directly into:

- `insight_extraction.md` — translating model behavior into decisions
- `limitations_and_tradeoffs.md` — documenting uncertainty and risks

Baseline models act as the **decision anchor** for the rest of Phase 4.
