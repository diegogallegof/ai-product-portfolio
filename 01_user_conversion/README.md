# User Conversion Case Study

## 1. Problem statement

A subscription-based streaming product is experiencing healthy top-of-funnel growth,
but overall paid conversion remains flat.

Despite multiple experiments across pricing, messaging, and onboarding,
it is unclear **which user behaviors actually predict conversion**
and where product intervention would have the highest impact.

The product team needs data-informed guidance to decide:
- Where to invest experimentation effort
- Which user segments to prioritize
- Which signals truly correlate with conversion (vs noise)

---

## 2. Product context

- Product type: Consumer streaming subscription
- Business model: Freemium → Paid subscription
- Primary KPI: Subscription conversion rate
- Secondary KPIs: Activation, retention, LTV proxy signals

Constraints:
- Limited experimentation capacity
- High risk of overfitting on historical cohorts
- Strong seasonality and behavioral variance

---

## 3. Key questions

This case study aims to answer:

1. Which user behaviors are most predictive of conversion?
2. At what point in the user lifecycle do these signals emerge?
3. How early can we reasonably predict conversion intent?
4. What trade-offs exist between model accuracy and product usability?
5. How should these insights influence product decisions?

---

## 4. Analytical approach (high level)

The analysis will focus on:

- Behavioral funnel analysis
- Feature exploration grounded in product logic
- Simple, interpretable models as decision-support tools
- Validation using holdout cohorts and temporal splits

The goal is **not** to build the most accurate model,
but the **most actionable** one.

---

## 5. Expected outputs

- Clear articulation of predictive signals
- Trade-offs between early vs late prediction
- Product recommendations informed by data
- Explicit assumptions and limitations

---

## 6. What this is not

- ❌ A Kaggle-style modeling exercise
- ❌ A production ML system
- ❌ A tutorial on algorithms

This is a **product-first data science case study**.

---
## Case structure

This case study is structured in clear analytical phases:

1. **Problem definition & product context**  
   High-level framing of the conversion problem.

2. **Analytical framing**  
   → See [`02_analytical_framing.md`](./02_analytical_framing.md)  
   Defines hypotheses, constraints, and decision questions before analysis.

3. **Signal definition & evaluation**  
   Identification and validation of behavioral signals.

4. **Modeling & insights**  
   Translating signals into actionable product insights.

5. **Recommendations**  
   Product decisions and experimentation guidance.

---
_Work in progress._
