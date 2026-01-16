# Signal Evaluation Plan

This document defines how behavioral signals will be evaluated, validated, and selected
to support product decisions related to subscription conversion.

The goal is not to maximize model performance, but to identify **reliable, interpretable,
and actionable signals** that can guide experimentation and product strategy.

---

## 1. Purpose of signal evaluation

Not all behavioral signals are equally useful.

A good signal must satisfy **three dimensions simultaneously**:

1. Predictive value — does it correlate with conversion?
2. Stability — does it behave consistently over time and cohorts?
3. Actionability — can product teams realistically act on it?

This plan establishes a structured framework to avoid:
- Overfitting to noisy behaviors
- Optimizing for vanity correlations
- Building models that do not translate into decisions

---

## 2. Evaluation principles

All signals will be evaluated under the following principles:

- **Product relevance over model complexity**
- **Causality awareness (correlation ≠ causation)**
- **Temporal integrity (no future leakage)**
- **Interpretability for stakeholders**
- **Decision impact over statistical perfection**

---

## 3. Evaluation dimensions

Each signal will be assessed across five core dimensions.

### 3.1 Predictive strength

Does the signal help discriminate between converters and non-converters?

Indicative metrics:
- Lift vs baseline conversion
- AUC delta when included in a simple model
- Mutual information with conversion outcome
- Univariate effect size

Signals with negligible or unstable predictive lift will be deprioritized.

---

### 3.2 Temporal validity & leakage risk

Signals must respect the decision timeline.

Checks include:
- Signal occurs strictly before conversion event
- Stability across time windows (D1, D3, D7, D14)
- No dependency on post-conversion behaviors
- No implicit exposure to paywall or pricing artifacts

Signals failing these checks are rejected regardless of predictive power.

---

### 3.3 Stability across cohorts

A useful signal should generalize.

Evaluation includes:
- Performance consistency across acquisition cohorts
- Sensitivity to country, platform, or traffic source
- Drift analysis over time

Signals that only work for a narrow segment may be:
- Flagged as **segment-specific**
- Excluded from global decisioning

---

### 3.4 Interpretability & explainability

Signals must be explainable to:
- Product managers
- Designers
- Growth and experimentation teams

Questions:
- Can the signal be described in plain language?
- Is its effect directionally intuitive?
- Can it be communicated without statistical caveats?

Black-box or opaque signals are penalized.

---

### 3.5 Actionability

A signal is only valuable if it can inform action.

We evaluate:
- Can product influence this behavior?
- Does it map to a surface (onboarding, messaging, pricing, UX)?
- Can it be targeted in experiments?

Signals with high predictive power but no clear action path are deprioritized.

---

## 4. Signal scoring framework

Each signal will be scored on a qualitative scale:

| Dimension            | Score |
|---------------------|-------|
| Predictive strength | Low / Medium / High |
| Temporal validity   | Pass / Risk / Fail |
| Stability           | Low / Medium / High |
| Interpretability    | Low / Medium / High |
| Actionability       | Low / Medium / High |

Final classification:
- **Keep** — strong candidate for modeling & decisioning
- **Conditional** — usable in specific contexts or segments
- **Drop** — not suitable for product decisions

---

## 5. Validation methodology

Signals will be validated using:

- Train / validation splits based on time (not random)
- Simple baseline models before complex ones
- Sensitivity analysis to confirm robustness
- Comparison against naive heuristics

This ensures that signals add value beyond obvious baselines.

---

## 6. Output of this phase

The outcome of signal evaluation is:

- A short list of **trusted signals**
- Clear rationale for inclusion or exclusion
- Inputs ready for modeling and insight generation
- Confidence that signals support real product decisions

This concludes Phase 3 and enables Phase 4: Modeling & Insights.

---

*Work in progress.*

