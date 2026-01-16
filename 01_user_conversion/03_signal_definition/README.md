# Signal Definition & Evaluation

This phase focuses on identifying, evaluating, and prioritizing **behavioral signals**
that may explain and predict subscription conversion.

The objective is **not** to engineer features or train models yet,
but to apply product judgment to decide **which signals are worth analyzing**.

A signal, in this context, is any observable user behavior that may:
- Indicate conversion intent
- Reflect product value realization
- Be influenced by product decisions or experiments

---

## Purpose of this phase

Before modeling or experimentation, it is critical to answer:

- Which user behaviors plausibly matter for conversion?
- Which signals are interpretable and stable enough to trust?
- Which signals can realistically inform product decisions?

This phase reduces noise, avoids overfitting,
and ensures downstream analysis remains **actionable**.

---

## How signals are evaluated

Signals are assessed using a structured evaluation framework that considers:

1. **Predictive value**  
   Does the signal meaningfully correlate with conversion?

2. **Stability**  
   Does it behave consistently across time, cohorts, and segments?

3. **Actionability**  
   Can product teams realistically act on this signal?

Signals that fail one or more of these criteria are deprioritized,
even if they appear statistically interesting.

For details, see:

→ **Signal evaluation framework:**  
[`signal_evaluation_plan.md`](./signal_evaluation_plan.md)

---

## Signal inventory

All candidate behavioral signals are documented and categorized in a centralized catalog,
including rationale, funnel stage, and potential product impact.

→ **Signals catalog:**  
[`signals_catalog.md`](./signals_catalog.md)

This catalog represents hypotheses, not conclusions.
Signals listed here are subject to validation and may be discarded later.

---

## What this phase deliberately avoids

- ❌ Feature engineering
- ❌ Model training
- ❌ Optimization for accuracy
- ❌ Correlation without product context

The output of this phase is **clarity**, not metrics.

---

## Outcome of this phase

By the end of signal definition, we expect to have:

- A short list of high-confidence behavioral signals
- Clear reasoning for why each signal matters
- Explicit trade-offs and assumptions documented

These outputs will directly inform the modeling and insight generation phase.

---
---

## Phase 3 summary

In this phase, we deliberately separated **signal ideation** from **signal validation**.

Rather than starting from available data or modeling techniques,
we applied product judgment to decide **which behaviors are worth analyzing at all**.

Key outcomes of this phase:

- A clearly documented **catalog of candidate behavioral signals**
- Explicit criteria to evaluate signals beyond raw predictive power
- Guardrails to avoid leakage, noise, and non-actionable correlations
- A shared language between product and data teams

Only signals that pass this evaluation framework will be considered in subsequent analysis.

This ensures that downstream modeling efforts remain:
- Interpretable
- Decision-oriented
- Aligned with real product levers

With Phase 3 complete, the analysis is ready to move from
**“what might matter”** to **“what actually drives decisions.”**

---

_Work in progress._
