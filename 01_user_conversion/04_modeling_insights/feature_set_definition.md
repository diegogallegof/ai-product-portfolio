# Feature Set Definition

This document defines how validated behavioral signals from Phase 3
are transformed into **model-ready features** for analysis in Phase 4.

The objective is not to maximize feature volume,
but to preserve **signal meaning, interpretability, and decision relevance**.

---

## 1) From signals to features

Signals represent **behaviors with product meaning**.
Features are **structured representations** of those behaviors used by models.

Key principle:
> Every feature must trace back to a documented signal and a plausible product decision.

If a feature cannot be explained in product terms,
it does not belong in this case study.

---

## 2) Feature design principles

All features adhere to the following principles:

1. **Traceability**
   - Each feature maps to a single signal (or a clearly defined aggregation).
2. **Temporal correctness**
   - Features only use information available **before** the prediction point.
3. **Interpretability**
   - Feature values and direction must be intuitive.
4. **Parsimony**
   - Prefer fewer, well-justified features over many weak ones.
5. **Stability**
   - Feature definitions should behave consistently across cohorts and time.

---

## 3) Feature groups

Features are grouped by **behavioral intent**, mirroring the signal taxonomy.

### 3.1 Activation features

Derived from activation-related signals.

Examples:
- `activated_d1` — binary flag indicating activation within first 24 hours
- `time_to_first_value` — continuous time delta to first meaningful action

Design notes:
- Binary features are preferred for early prediction windows
- Time-based features are capped or bucketed to reduce noise

---

### 3.2 Engagement depth features

Derived from early engagement behaviors.

Examples:
- `core_actions_7d` — count of core actions in first 7 days
- `active_days_7d` — number of distinct active days in first 7 days

Design notes:
- Use short windows (D3, D7) to balance early signal vs reliability
- Consider log or capped transforms to avoid domination by heavy users

---

### 3.3 Habit formation features

Derived from repeated or patterned usage.

Examples:
- `consecutive_active_days_max`
- `usage_time_of_day_consistency` — low variance in session start times

Design notes:
- Habit features are typically weaker early but stronger later
- Often evaluated conditionally (e.g., only after activation)

---

### 3.4 Intent features

Derived from explicit monetization-related behaviors.

Examples:
- `premium_page_visit_14d` — binary flag
- `paywall_impressions_14d` — count of paywall exposures
- `payment_start_flag` — binary indicator of checkout initiation

Design notes:
- Binary features often outperform raw counts for interpretability
- Non-linear effects are expected (e.g., too many impressions can hurt)

---

### 3.5 Friction & trust features

Derived from error, hesitation, or support-seeking behaviors.

Examples:
- `checkout_error_count`
- `help_view_near_checkout` — binary flag

Design notes:
- Often have **negative** or conditional effects
- Interpretation must consider context (e.g., help + conversion)

---

## 4) Feature windows and prediction timing

Features are computed relative to **prediction cutoffs**, not globally.

Typical windows:
- **Early:** D1 / D3 — high actionability, lower confidence
- **Mid:** D7 — balance of signal strength and timeliness
- **Late:** D14 — stronger signals, less opportunity to intervene

Trade-offs between early and late prediction are explicitly evaluated
in downstream modeling.

---

## 5) Feature exclusions

The following are intentionally excluded:

- Post-conversion behaviors
- Features derived from pricing outcomes
- Features encoding experiment assignment
- Highly correlated duplicates with no added insight

Exclusions are documented to prevent silent leakage.

---

## 6) Feature documentation standard

Each feature must be documented with:

- Source signal
- Definition and time window
- Expected directional effect
- Known risks or caveats
- Potential product levers

Undocumented features are not eligible for modeling.

---

## 7) Relationship to modeling

This feature set feeds directly into:
- `baseline_models.md`
- `insight_extraction.md`

Only features defined here are used in modeling,
ensuring traceability and interpretability throughout Phase 4.

---

_Work in progress._
