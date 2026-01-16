# Signals Catalog

This document defines and catalogs all behavioral signals considered for subscription conversion analysis.

The purpose of this catalog is **not** to list every available event, but to explicitly document:
- Which signals are *considered meaningful*
- Why they exist from a product perspective
- How they are expected to relate to conversion behavior

This catalog serves as the **source of truth** for signal selection before any modeling begins.

---

## 1. What is a “signal”?

In this case study, a **signal** is defined as:

> A user behavior that plausibly reflects intent, engagement, or readiness to convert,  
> and that can be observed consistently and acted upon by product teams.

A signal is **not**:
- A raw event without context
- A feature engineered only for model performance
- A metric chosen solely because it improves accuracy

---

## 2. Signal inclusion criteria

A signal is included in this catalog only if it satisfies **at least one** of the following:

- Reflects **user intent** (explicit or implicit)
- Represents **meaningful engagement**, not passive activity
- Occurs **before conversion**, not as a consequence of it
- Can inform **product decisions or experiments**

Signals that are purely descriptive, redundant, or non-actionable are intentionally excluded.

---

## 3. Signal taxonomy

Signals are grouped by **behavioral meaning**, not technical implementation.

### 3.1 Activation signals  
Early behaviors indicating initial value realization.

Examples:
- First successful content interaction
- Completion of onboarding flow
- First session exceeding a minimum duration

---

### 3.2 Engagement depth signals  
Behaviors reflecting repeated or deep product usage.

Examples:
- Number of active days in first N days
- Content consumption frequency
- Session depth or duration patterns

---

### 3.3 Habit formation signals  
Indicators that usage is becoming routine.

Examples:
- Consecutive-day usage
- Time-of-day consistency
- Repeated use of the same feature or content type

---

### 3.4 Intent signals  
Explicit or implicit indicators of purchase consideration.

Examples:
- Viewing pricing or paywall screens
- Attempting locked actions
- Triggering upgrade prompts

---

### 3.5 Friction and dropout signals  
Behaviors suggesting hesitation, confusion, or disengagement.

Examples:
- Abandoned onboarding steps
- Repeated failed actions
- Sudden drop in usage after initial engagement

---

## 4. Signal catalog (initial list)

> This section documents **candidate signals**, not final selections.

Each signal is described using a consistent template to enforce clarity and comparability.

---

### Signal ID: S01  
**Name:** Early activation achieved  
**Category:** Activation  

**Description:**  
User completes a meaningful first action that demonstrates initial product value.

**Product rationale:**  
Users who experience value early are more likely to consider upgrading.

**Expected relationship to conversion:**  
Positive correlation.

**Notes / risks:**  
Activation definitions may vary across cohorts.

---

### Signal ID: S02  
**Name:** High engagement frequency (early)  
**Category:** Engagement depth  

**Description:**  
User interacts with core features multiple times within the first X days.

**Product rationale:**  
Repeated usage suggests perceived value beyond novelty.

**Expected relationship to conversion:**  
Positive, with diminishing returns.

**Notes / risks:**  
May correlate with availability or time bias rather than intent.

---

## 5. Explicit exclusions

The following types of signals are **intentionally excluded**:

- Signals occurring **after** conversion
- Signals derived from pricing experiments
- Signals that cannot be influenced by product changes
- Signals that exist only due to logging artifacts

This prevents leakage and false confidence.

---

## 6. Relationship to evaluation

This catalog **does not rank or validate signals**.

Validation, stability testing, and prioritization are handled separately in:

→ `signal_evaluation_plan.md`

Only signals documented here are eligible for evaluation.

---

## 7. Status

This catalog is a **living document**.

Signals may be:
- Added when new hypotheses emerge
- Deprecated if found unstable or non-actionable
- Refined as product understanding improves
