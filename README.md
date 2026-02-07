# AI Product Portfolio — User Conversion Case Study

This repository documents an applied AI Product case study at the intersection of
**Product Management, Data Science, and AI**, focused on **subscription conversion**
in streaming-style consumer products.

The goal of this case study is **not** to showcase advanced models or
production-ready ML systems, but to demonstrate **how data and machine learning
can responsibly support product decisions** under real-world constraints.

This work reflects how I think as a Product Manager when using data and AI
to reason about uncertainty, trade-offs, and decision impact.

My background spans engineering, software development, and over a decade building
and operating subscription and streaming products at scale. This case study reflects
a **product-first approach to AI**: prioritizing metrics, assumptions, limitations,
and downstream decisions over raw model performance.

---

## 🎯 Case study objective

The objective of this case study is to explore:

> *How can we estimate and reason about a user’s likelihood to convert to a paid
subscription using realistic behavioral signals — and how should a product team
act on that information?*

Rather than optimizing for accuracy alone, the focus is on building a
**decision-support system** that helps answer questions such as:

- Which user behaviors meaningfully signal conversion intent?
- Where should a product intervene — and where should it not?
- What assumptions are embedded in our modeling choices?
- What risks do these decisions introduce?

---

## 📂 Repository structure

The case study follows a structured, end-to-end flow:

```text
01_user_conversion/
├── 02_analytical_framing/     # Business framing, hypotheses, trade-offs
├── 03_signal_definition/      # Behavioral signals and evaluation criteria
├── 04_modeling_insights/      # Modeling approach, insights, limitations
├── 05_recommendations/        # Decision framework and experimentation plan
├── data/                      # Synthetic data generator and dataset
├── notebooks/                 # EDA and baseline model training
├── models/                    # Persisted model artifacts
