# Experiment Design

This document outlines how each product recommendation
would be **validated through controlled experimentation**.

The goal is to reduce uncertainty by testing:
- Whether the recommendation produces measurable lift
- Under what conditions it works or fails
- What unintended effects may emerge

Experiments are designed to be **pragmatic, scoped, and decision-oriented**.

---

## Experimentation principles

All experiments in this phase follow these principles:

1. **Hypothesis-driven**  
   Each experiment tests a clear, falsifiable hypothesis.

2. **Minimal viable scope**  
   Experiments are scoped to isolate the effect of the recommendation.

3. **User-safe by design**  
   All experiments are reversible and monitored for negative impact.

4. **Decision-focused**  
   Results are evaluated based on decision value, not statistical perfection.

---

## Experiment 1 — Monetization after value realization

### Linked recommendation
Sequence monetization after early value realization

### Hypothesis
Delaying monetization prompts until users complete a value realization event
will increase overall subscription conversion without harming engagement.

### Experiment design
- **Type:** A/B test
- **Control:** Immediate or early paywall exposure
- **Variant:** Paywall shown only after activation signal
- **Population:** New users (Day 0–7)
- **Randomization:** User-level

### Primary metrics
- Subscription conversion rate
- Activation completion rate

### Secondary metrics
- Time to conversion
- Early retention (D7)

### Duration
- 2–3 weeks or until statistical stability

---

## Experiment 2 — Mid-early lifecycle intervention (D3–D7)

### Linked recommendation
Prioritize mid-early intent signals for intervention

### Hypothesis
Targeting conversion interventions during the D3–D7 window
will yield higher lift than immediate onboarding or late-stage pushes.

### Experiment design
- **Type:** A/B/C test
- **Variants:**  
  - Early (D0–D1)  
  - Mid-early (D3–D7)  
  - Late (D8+)
- **Population:** Activated but non-converting users

### Primary metrics
- Conversion rate by cohort
- Incremental lift vs control

### Secondary metrics
- Engagement depth
- Message interaction rate

### Duration
- 3–4 weeks

---

## Experiment 3 — Monetization exposure frequency caps

### Linked recommendation
Cap monetization exposure to avoid saturation effects

### Hypothesis
Introducing frequency caps on monetization surfaces
will reduce user fatigue and improve net conversion.

### Experiment design
- **Type:** A/B test
- **Control:** Unlimited or existing exposure rules
- **Variant:** Frequency-capped exposure
- **Population:** High-engagement non-converters

### Primary metrics
- Conversion rate
- Monetization interaction rate

### Secondary metrics
- Session abandonment
- Short-term churn

### Duration
- 2–3 weeks

---

## Experiment 4 — Checkout friction reduction

### Linked recommendation
Treat friction reduction as a primary conversion lever

### Hypothesis
Reducing checkout errors and friction
will increase conversion among high-intent users more than additional messaging.

### Experiment design
- **Type:** Before/after or A/B (where feasible)
- **Variant:** Improved error handling / retry flows
- **Population:** Users initiating payment

### Primary metrics
- Successful payment completion rate
- Error rate per attempt

### Secondary metrics
- Drop-off during checkout
- Support or help-seeking events

### Duration
- 2–4 weeks

---

## Experiment 5 — Personalized monetization using intent signals

### Linked recommendation
Personalize monetization using intent signals

### Hypothesis
Personalized monetization timing and messaging
will outperform uniform monetization strategies.

### Experiment design
- **Type:** A/B test
- **Control:** Static monetization rules
- **Variant:** Intent-based personalization
- **Population:** Activated users with intent signals

### Primary metrics
- Conversion rate
- Revenue per exposed user

### Secondary metrics
- Engagement post-exposure
- Fatigue indicators

### Duration
- 3–4 weeks

---

## Experiment evaluation criteria

Experiments are evaluated on:
- Directional lift
- Consistency across segments
- Absence of severe negative side effects

Statistical significance is considered,
but **decision confidence** is the primary goal.

---

## Summary

This experimentation plan ensures that:
- Each recommendation is validated empirically
- Risks are identified early
- Decisions can be iterated or reversed safely

It bridges the gap between insight and execution.
