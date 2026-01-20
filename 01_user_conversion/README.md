# User Conversion Case Study  
**AI Product & Product-First Data Science**

This repository presents a **product-first data science case study**
focused on understanding and improving **subscription conversion**
in a consumer streaming product.

The work reflects how an **AI Product Manager / Data-informed PM**
approaches an ambiguous business problem:
by framing the right questions, identifying meaningful behavioral signals,
making explicit trade-offs, and translating insights into decisions.

---

## 1. Problem statement

A subscription-based streaming product is experiencing healthy top-of-funnel growth,
but overall paid conversion remains flat.

Despite multiple experiments across pricing, messaging, and onboarding,
it is unclear:

- **Which user behaviors actually predict conversion**
- **When conversion intent meaningfully emerges**
- **Where product intervention has the highest leverage**

The product team needs data-informed guidance to decide:
- Where to invest experimentation effort
- Which user segments to prioritize
- Which signals truly correlate with conversion (vs noise)

---

## 2. Product context

- **Product type:** Consumer streaming subscription
- **Business model:** Freemium → Paid subscription
- **Primary KPI:** Subscription conversion rate
- **Secondary KPIs:** Activation, retention, LTV proxy signals

### Constraints
- Limited experimentation capacity
- High risk of overfitting on historical cohorts
- Strong seasonality and behavioral variance

These constraints shape both the analytical approach
and the type of recommendations that are feasible in practice.

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

The analysis follows a **product-first data science approach**:

- Behavioral funnel analysis grounded in real user flows
- Signal exploration driven by product intuition, not data availability alone
- Simple, interpretable models used as decision-support tools
- Validation through cohort analysis and temporal splits

The goal is **not** to build the most accurate model,
but the **most actionable and explainable** one.

---

## 5. What this case study demonstrates

This project showcases how an AI Product or Data-informed PM:

- Frames problems before modeling
- Distinguishes signal from noise
- Balances interpretability and accuracy
- Makes uncertainty and limitations explicit
- Translates insights into concrete product decisions

---

## 6. What this is — and what it is not

**This is:**
- A product-driven data science case study
- A realistic decision-making framework under uncertainty
- A demonstration of applied AI thinking in a product context

**This is not:**
- ❌ A Kaggle-style modeling exercise
- ❌ A production ML system
- ❌ A tutorial on algorithms

---

## 7. Case structure

This case study is organized into clear analytical and decision-making phases:

1. **Problem definition & product context**  
   This document (`README.md`)

2. **Analytical framing**  
   → [`02_analytical_framing/`](./02_analytical_framing/)  
   Hypotheses, assumptions, constraints, and decision questions.

3. **Signal definition & evaluation**  
   → [`03_signal_definition/`](./03_signal_definition/)  
   Identification, validation, and prioritization of behavioral signals.

4. **Modeling & insights**  
   → [`04_modeling_insights/`](./04_modeling_insights/)  
   Interpretable modeling and extraction of product-relevant insights.

5. **Product recommendations**  
   → [`05_recommendations/`](./05_recommendations/)  
   Decision framework, recommendations, experiment design, success metrics, and risks.

Each phase is documented to preserve **clarity, traceability, and intent**.

---

## 8. Status

This is a living portfolio project.
Future extensions may include:
- Execution simulations
- Additional case studies (retention, pricing, monetization)
- Lightweight modeling notebooks using synthetic data

Feedback and discussion are welcome.
