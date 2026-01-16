# Signal Evaluation Plan

This document defines how behavioral signals will be evaluated, validated, and selected
to support subscription conversion decisions.

The objective is **not** to maximize model performance,
but to identify **reliable, interpretable, and actionable signals**
that can guide product strategy and experimentation.

---

## 1. Purpose of signal evaluation

Not all behavioral signals are equally useful.

A strong signal must satisfy **three dimensions simultaneously**:

1. **Predictive value** — does it meaningfully relate to conversion?
2. **Stability** — does it behave consistently over time and cohorts?
3. **Actionability** — can product teams realistically act on it?

This plan exists to avoid:
- Optimizing for noise or vanity correlations
- Overfitting to historical cohorts
- Building models that do not translate into decisions

---

## 2. Evaluation principles

All signals are evaluated under the following principles:

- Product relevance over statistical sophistication
- Temporal integrity (no future leakage)
- Interpretability for non-technical stakeholders
- Decision impact over marginal accuracy gains

---

## 3. Quantitative evaluation dimensions

Each signal is evaluated across five dimensions.
Thresholds are indicative and may be adjusted based on data availability.

---

### 3.1 Predictive strength

**Question:** Does the signal help discriminate between converters and non-converters?

**Primary checks:**
- Conversion rate lift vs baseline
- AUC delta when added to a simple baseline model
- Effect size consistency across bins or percentiles

**Indicative thresholds:**
- Meaningful conversion lift: **≥ +5–10% relative**
- AUC delta (single-signal model): **≥ +0.02**
- Effect direction stable across cohorts

**Fail conditions:**
- No lift or highly volatile effect
- Signal only performs in one narrow slice

---

### 3.2 Temporal validity & leakage risk

**Question:** Does the signal respect the decision timeline?

**Checks:**
- Signal occurs strictly **before** conversion
- No dependency on post-paywall or post-payment events
- Stable behavior across time windows (D1, D3, D7, D14)

**Fail conditions:**
- Signal appears only after monetization exposure
- Signal implicitly encodes future knowledge

Any signal failing this check is **automatically dropped**.

---

### 3.3 Stability across cohorts

**Question:** Does the signal generalize?

**Checks:**
- Consistent effect across acquisition cohorts
- Similar behavior across platform or geography (when applicable)
- Limited drift over time

**Indicative thresholds:**
- Effect direction consistent in ≥ 70% of cohorts
- No single cohort drives the majority of signal strength

**Fail conditions:**
- Strong effect in one cohort, absent or inverted elsewhere

---

### 3.4 Interpretability

**Question:** Can the signal be explained clearly?

**Checks:**
- Clear behavioral description in plain language
- Intuitive directional effect
- Explainable without statistical caveats

**Fail conditions:**
- Signal cannot be explained without model internals
- Effect contradicts product intuition with no clear rationale

Interpretability is required for signals used in product decisioning,
even if they show predictive strength.

---

### 3.5 Actionability

**Question:** Can product teams realistically act on this signal?

**Checks:**
- Signal maps to a controllable product surface
- Can inform experiments, UX changes, or messaging
- Can be segmented or targeted meaningfully

**Fail conditions:**
- No clear product lever
- Signal describes an outcome rather than a behavior

---

## 4. Signal scoring framework

Each signal is scored qualitatively:

| Dimension            | Score options        |
|---------------------|----------------------|
| Predictive strength | Low / Medium / High  |
| Temporal validity   | Pass / Risk / Fail   |
| Stability           | Low / Medium / High  |
| Interpretability    | Low / Medium / High  |
| Actionability       | Low / Medium / High  |

---

## 5. Decision rules

Final classification rules:

- **Keep**
  - Predictive strength: Medium or High
  - Temporal validity: Pass
  - Stability: Medium or High
  - Actionability: Medium or High

- **Conditional**
  - Predictive strength: Medium
  - Stability issues or segment-specific behavior
  - Useful for targeted experiments only

- **Drop**
  - Temporal validity: Fail
  - Predictive strength: Low
  - No clear action path

---

## 6. Validation methodology

Signals are validated using:

- Time-based train / validation splits
- Simple baseline models before complex ones
- Sensitivity checks across cohorts
- Comparison against naive heuristics

Signals must prove value beyond obvious baselines.

---

## 7. Output of this phase

The outcome of signal evaluation is:

- A short list of **trusted signals**
- Explicit rationale for inclusion or exclusion
- Inputs ready for modeling and insight generation
- Confidence that signals support real product decisions

This concludes Phase 3 and enables Phase 4: Modeling & Insights.

---

_Work in progress._
