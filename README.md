# AI Product Portfolio  
**Applied AI Systems for Product Decision-Making**

This repository documents applied AI case studies at the intersection of  
**Product Management, Data Science, and Systems Architecture**,  
focused on subscription-driven consumer products.

Rather than showcasing isolated models, this portfolio demonstrates how
machine learning becomes a structured **decision-support system**
within real product environments.

The emphasis is not on model complexity —
but on clarity, interpretability, and operational alignment.

---

# 🎯 Portfolio Objective

The purpose of this portfolio is to answer a core question:

> How do we responsibly translate behavioral data into structured product decisions?

Each case study moves deliberately through:

- Problem framing
- Signal design
- Interpretable modeling
- Explicit policy logic
- Decision architecture
- Operational exposure (API layer)

The goal is to show how AI becomes an instrument of product reasoning —
not a black-box optimization engine.

---

# 📌 Featured Case Study

## 01 — User Conversion Decision System

A structured exploration of subscription conversion in a streaming-style product.

This case study evolved from:

Analytical exploration  
→ Interpretable modeling  
→ Persisted model artifact  
→ FastAPI scoring service  
→ Explicit decision layer (policy thresholds)  

It demonstrates how model outputs are intentionally separated
from business policy logic.

### Core Principle

> Models produce probabilities. Products operate on decisions.

---

# 🧠 What This Portfolio Demonstrates

Across projects, this repository highlights the ability to:

- Frame ambiguous growth problems before modeling
- Design behavioral signals grounded in product context
- Prefer interpretability over marginal accuracy gains
- Separate statistical inference from decision policy
- Build modular AI systems aligned with experimentation strategy
- Move from analysis to operational architecture

This reflects how an AI Product leader reasons about uncertainty,
trade-offs, and downstream impact.

---

# 🏗️ Architectural Thinking

Each case study emphasizes layered design:

Signals
↓
Model
↓
Probability
↓
Decision Policy
↓
Product Action


Where appropriate, systems are exposed through lightweight API layers
to demonstrate operational viability.

The focus is structured reasoning — not infrastructure scale.

---

# 📂 Repository Structure

```text
01_user_conversion/
├── 02_analytical_framing/      # Business framing and trade-offs
├── 03_signal_definition/       # Behavioral signal design
├── 04_modeling_insights/       # Interpretable modeling
├── 05_recommendations/         # Decision logic and experiment design
├── app/                        # FastAPI scoring + decision layer
├── data/                       # Synthetic dataset generator
├── models/                     # Persisted model artifacts
├── notebooks/                  # EDA and baseline training
