# User Conversion Case Study  
**AI Product Decision System | Product-First Data Science**

This repository presents a **product-first AI case study**
focused on understanding and improving **subscription conversion**
in a consumer streaming product.

The project evolved from analytical exploration to a structured
**decision-support system** that transforms behavioral signals into
actionable product segments.

This reflects how an **AI Product Manager / Decision-Oriented PM**
approaches ambiguous growth problems:
by framing the right questions, identifying meaningful behavioral signals,
making explicit trade-offs, and translating model outputs into decisions.

---

# 1. Problem statement

A subscription-based streaming product is experiencing healthy top-of-funnel growth,
but paid conversion remains flat.

Despite experimentation across pricing, onboarding, and messaging,
it is unclear:

- Which user behaviors truly signal conversion intent
- When meaningful intent emerges in the lifecycle
- Where product intervention creates the highest leverage

The product team needs structured, data-informed guidance to decide:

- Where to focus experimentation effort
- Which segments to prioritize
- How to operationalize model outputs safely

---

# 2. From analysis to decision system

This project is intentionally structured in two layers:

### Analytical Layer
- Signal definition
- Behavioral validation
- Interpretable modeling (logistic regression baseline)

### Decision Layer
- Probability → Policy thresholds
- Explicit segmentation bands
- Clear separation between model logic and business logic

The goal is not to maximize predictive accuracy,
but to build a **usable, interpretable, and product-aligned decision framework.**

---

# 3. Architecture Overview

The project now includes:

- Synthetic but realistic behavioral dataset
- Interpretable baseline model (scikit-learn pipeline)
- Persisted model artifact (`.joblib`)
- FastAPI scoring service
- Explicit Decision Engine translating probability into action segments

High-level flow:

User Signals
↓
Model (predict_proba)
↓
Conversion Probability
↓
Decision Policy (threshold bands)
↓
Action Segment


This explicit separation avoids entangling statistical outputs
with product rules.

---

# 4. Key product questions addressed

1. Which user behaviors most predict conversion?
2. How early can we detect intent?
3. What is the trade-off between interpretability and accuracy?
4. How should probabilities be converted into operational segments?
5. How can decision logic remain transparent and adjustable?

---

# 5. Technical implementation

## Data
- Synthetic but structured dataset
- Behavioral signals aligned with streaming context
- Logistic probability generation with noise and tier effects

## Model
- Logistic Regression baseline
- Interpretable coefficients
- Pipeline encapsulating preprocessing + estimator
- Persisted model artifact

## API Layer
- FastAPI application
- Pydantic schema validation
- `/health` and `/score` endpoints
- Automatic OpenAPI documentation

## Decision Layer
- Explicit threshold-based segmentation
- Model logic separated from business policy
- Designed for controlled experimentation

---

# 6. What this case study demonstrates

This project showcases how an AI Product or Data-informed PM:

- Frames problems before modeling
- Designs signals intentionally
- Uses interpretable models as decision-support tools
- Separates statistical inference from business policy
- Makes assumptions and trade-offs explicit
- Moves from analysis to operational system

---

# 7. What this is — and what it is not

## This is:
- A product-driven AI decision system
- A realistic applied ML architecture
- A demonstration of operational AI thinking

## This is not:
- ❌ A Kaggle competition model
- ❌ A deep learning showcase
- ❌ A production-scale MLOps pipeline

The focus is clarity, reasoning, and product alignment.

---

# 8. Case structure

1. Problem definition & context  
2. Analytical framing  
3. Signal definition  
4. Modeling & insights  
5. Product recommendations  
6. API & decision layer implementation  

Each phase preserves traceability between:

**Problem → Signal → Model → Decision → Recommendation**

---

# 9. Current status

This project now includes:

- End-to-end scoring API
- Decision segmentation layer
- Modular architecture ready for extension

Planned extensions:

- Policy versioning
- Decision experimentation simulation
- Lightweight deployment
- Additional case studies (retention, monetization, lifecycle)

---

Feedback and discussion are welcome.
