# Insight Extraction

This document translates model outputs and signal behavior
into **product-relevant insights** that can inform decision-making.

The objective is not to report metrics,
but to explain **what is happening, why it is happening,
and what product teams should do differently**.

---

## 1) From model output to insight

Models produce coefficients, splits, and scores.
Insights translate those artifacts into **clear statements about user behavior**.

An insight must:
- Be grounded in validated signals
- Be explainable in plain language
- Imply a potential product action or trade-off

If a finding cannot be expressed as a behavioral insight,
it is not considered useful for this case study.

---

## 2) Core questions guiding insight extraction

All insights are derived by answering the following questions:

1. Which signals consistently explain conversion outcomes?
2. Which signals matter early vs late in the user lifecycle?
3. Which combinations of signals amplify or suppress conversion?
4. Where do diminishing returns or negative effects appear?
5. What behaviors are **necessary but not sufficient** for conversion?

---

## 3) Insight categories

Insights are grouped by **decision relevance**, not by model type.

---

### 3.1 Primary drivers of conversion

These are signals that:
- Appear consistently across models
- Show stable directionality
- Explain a meaningful portion of variance

Example insight format:
> Users who achieve early activation and exhibit repeated engagement
> within the first 7 days are significantly more likely to convert,
> regardless of acquisition source.

Implication:
- Early value realization is a prerequisite for monetization efforts.

---

### 3.2 Conditional and interaction effects

Some signals matter **only when combined with others**.

Examples:
- Intent signals are strong only after activation
- High engagement without value realization does not increase conversion

Example insight format:
> Premium page visits increase conversion probability
> primarily among users who have already experienced core product value.

Implication:
- Monetization prompts should be sequenced after activation, not before.

---

### 3.3 Early vs late prediction trade-offs

Insights are extracted across multiple prediction windows (D1, D3, D7, D14).

Typical findings:
- Early windows favor actionability but lower confidence
- Later windows improve accuracy but reduce intervention opportunity

Example insight format:
> While conversion can be predicted more accurately at D14,
> the majority of actionable uplift is available by D7.

Implication:
- Product interventions should prioritize mid-early signals.

---

### 3.4 Saturation and diminishing returns

Some signals exhibit non-linear behavior.

Examples:
- Too many paywall impressions reduce conversion likelihood
- Engagement plateaus beyond a certain threshold

Example insight format:
> Conversion likelihood increases with paywall exposure up to a point,
> after which additional exposure correlates with lower conversion.

Implication:
- Monetization surfaces require frequency caps and personalization.

---

### 3.5 Friction and trust breakdowns

Negative or suppressive signals highlight where the funnel breaks.

Examples:
- Checkout errors
- Repeated failed actions
- Help-seeking near payment without resolution

Example insight format:
> Users encountering checkout errors show a sharp drop in conversion,
> even when intent signals are strong.

Implication:
- Reducing friction can yield higher ROI than increasing intent messaging.

---

## 4) Confidence and robustness checks

Each insight is evaluated for robustness:

- Consistency across cohorts and time splits
- Stability across baseline model variants
- Sensitivity to feature definitions

Insights that fail robustness checks are documented but deprioritized.

---

## 5) Insight documentation standard

Each accepted insight is documented with:

- **Insight statement**
- **Signals involved**
- **Prediction window**
- **Confidence level** (High / Medium / Exploratory)
- **Product implication**

This standard ensures traceability and avoids overinterpretation.

---

## 6) What this phase deliberately avoids

- Reporting isolated metrics without interpretation
- Treating correlation as causation
- Overgeneralizing segment-specific effects
- Optimizing insights for storytelling rather than truth

---

## 7) Relationship to recommendations

Insights generated here directly inform:
- Experiment design
- Prioritization of product work
- Monetization strategy adjustments

They form the evidence base for **Phase 5: Recommendations**.
