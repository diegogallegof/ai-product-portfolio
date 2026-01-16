# Data Design & Metric Definitions

This document defines the data model, metrics, and assumptions
used in the User Conversion Case Study.

The purpose is to ensure analytical clarity before any modeling or exploration.

---

## 1. Unit of analysis

Primary unit:
- **User**

Secondary units:
- Session
- Event
- Day (for temporal aggregation)

All modeling and metrics will be aligned to the **user-level outcome**.

---

## 2. Target variable

**Subscription conversion**

Definition:
- Binary outcome: user converts to paid subscription within a defined time window

Assumptions:
- Conversion is final for the purposes of this analysis
- Refunds and chargebacks are ignored
- Trial-to-paid is considered conversion

Time window:
- Conversion within 30 days of first app open

---

## 3. Candidate behavioral signals

The following categories are considered as potential predictors:

### a) Activation signals
- First content consumed
- Time to first meaningful action
- Completion of onboarding steps

### b) Engagement signals
- Number of active days
- Sessions per day
- Content consumption depth

### c) Friction signals
- Ads encountered
- Errors or failed attempts
- Drop-offs during key flows

### d) Intent signals
- Visits to paywall or pricing screens
- Repeated exposure to upgrade prompts
- Interaction with subscription CTAs

---

## 4. Features intentionally excluded

The following data is intentionally excluded to reduce noise and leakage:

- Post-conversion behavior
- Marketing attribution data
- Demographic or inferred personal data
- Features unavailable in early lifecycle

---

## 5. Temporal considerations

- Features will be computed using **only data available up to prediction time**
- Separate feature windows will be tested (Day 1, Day 3, Day 7)
- No look-ahead bias is allowed

---

## 6. Metric philosophy

Primary evaluation criteria:
- Interpretability
- Stability across cohorts
- Alignment with product decision-making

Secondary criteria:
- Predictive lift
- Precision vs recall trade-offs

Accuracy alone is not sufficient.

---

## 7. Known limitations

- Synthetic or anonymized data
- Simplified subscription logic
- No causal inference claims

All conclusions must be framed as **decision support**, not truth.

---

_This document is intentionally written before any data exploration._
