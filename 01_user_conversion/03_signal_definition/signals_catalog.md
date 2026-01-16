# Signal Catalog

This document defines the **candidate behavioral signals** evaluated to understand and predict subscription conversion.

Signals are treated as **decision-support inputs**, not as features by default.
Each signal must justify its inclusion through clarity, interpretability, and product relevance.

---

## Signal design principles

All signals in this catalog follow these principles:

- Must represent **intent or value realization**, not raw activity
- Must be **actionable** from a product or experimentation perspective
- Must be **measurable early enough** to influence decisions
- Must be evaluated against simple baselines before modeling
- Correlation alone is insufficient — context and causality matter

---

## Signal taxonomy

Signals are grouped by the type of user behavior they represent.

### 1. Activation signals
Early behaviors that indicate whether a user has reached initial value.

Examples:
- First successful content consumption
- Completion of onboarding flow
- First meaningful interaction with core features

---

### 2. Engagement depth signals
Behaviors that capture **how deeply** a user interacts with the product.

Examples:
- Sessions per day / week
- Content consumption volume
- Diversity of content interacted with

---

### 3. Habit formation signals
Patterns that suggest repeat usage and routine building.

Examples:
- Consecutive active days
- Time-of-day consistency
- Week-over-week activity stability

---

### 4. Monetization proximity signals
Behaviors that indicate closeness to a paid decision.

Examples:
- Paywall views
- Pricing

