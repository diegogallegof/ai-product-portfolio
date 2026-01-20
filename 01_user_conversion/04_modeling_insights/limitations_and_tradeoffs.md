# Limitations and Trade-offs

This document explicitly documents the limitations, risks, and trade-offs
associated with the modeling and insights generated in this case study.

The purpose is not to weaken conclusions,
but to ensure **honest decision-making under uncertainty**.

---

## 1) Why limitations matter

All models and insights are approximations of reality.

Ignoring limitations leads to:
- Overconfidence in weak signals
- Misaligned product investments
- Fragile decisions that fail under change

Documenting limitations is a **core part of responsible product and data practice**.

---

## 2) Data and measurement limitations

### 2.1 Event instrumentation quality

- Some behaviors may be under-logged or inconsistently logged
- Event definitions may evolve over time
- Missing or delayed events can bias early-window features

**Implication:**  
Signal strength should be interpreted directionally, not as absolute truth.

---

### 2.2 Proxy behavior risks

Several signals act as **proxies**, not direct measures.

Examples:
- Engagement as a proxy for value
- Paywall exposure as a proxy for intent

**Risk:**  
Proxies may correlate without representing causal mechanisms.

**Mitigation:**  
Insights are validated across cohorts and interpreted conservatively.

---

## 3) Temporal trade-offs

### 3.1 Early vs late prediction

- Early prediction (D1–D3):
  - Higher actionability
  - Lower confidence
- Late prediction (D7–D14):
  - Higher confidence
  - Reduced intervention window

**Trade-off:**  
Optimizing for accuracy often conflicts with the ability to act.

**Decision stance:**  
Prefer **slightly weaker early signals** if they enable meaningful intervention.

---

### 3.2 Signal degradation over time

Signals that are predictive today may weaken as:
- Product UX changes
- User behavior adapts
- Monetization strategies evolve

**Implication:**  
Signals require periodic re-validation.

---

## 4) Generalization risks

### 4.1 Cohort-specific effects

Some insights may be driven by:
- Specific acquisition channels
- Geographic or cultural factors
- Platform-specific UX

**Risk:**  
Applying insights globally may reduce effectiveness.

**Mitigation:**  
Insights are treated as hypotheses for targeted experimentation.

---

### 4.2 Historical bias

Models are trained on historical data,
which may encode past product decisions and constraints.

**Risk:**  
Optimizing against history may limit innovation.

**Mitigation:**  
Use insights to inform experiments, not to lock in static strategies.

---

## 5) Modeling limitations

### 5.1 Interpretability vs performance

By design, this case study favors:
- Simpler models
- Clear explanations
- Stable insights

**Trade-off:**  
Some non-linear patterns may remain unexplored.

**Decision stance:**  
Interpretability is prioritized for product decisioning.

---

### 5.2 Absence of causal inference

This analysis identifies **associations**, not causation.

**Risk:**  
Misinterpreting correlation as causation.

**Mitigation:**  
Insights are framed as inputs to experimentation, not final answers.

---

## 6) Decision-making implications

Given these limitations:

- Insights should guide **what to test**, not dictate outcomes
- Product teams should monitor signal drift over time
- High-impact decisions should be validated experimentally

Models are tools for **reducing uncertainty**, not eliminating it.

---

## 7) What would improve confidence

Additional steps that would strengthen conclusions include:

- Controlled experiments targeting key signals
- Longer-term retention and LTV tracking
- Improved event instrumentation
- Segment-specific deep dives

---

## 8) Summary

This case study intentionally trades:
- Maximum accuracy
for
- Interpretability, robustness, and actionability

The resulting insights are best used as:
- Directional guidance
- Experimentation inputs
- Decision support under uncertainty

This concludes **Phase 4: Modeling & Insights**.
