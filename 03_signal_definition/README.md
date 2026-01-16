# Signal Definition & Evaluation (Phase 3)

This phase defines **what we will treat as a meaningful signal** for subscription conversion, and how we will validate that signals are:
- measurable
- stable
- not leaking the label
- actionable for product decisions

The goal is not to “create features” blindly — it is to separate **signal vs noise** before modeling.

---

## 1) What we mean by “signal”
A **signal** is a user behavior or attribute that:
1) occurs **before** conversion (temporal correctness)
2) has a plausible **product mechanism** (why it would influence conversion)
3) can be **instrumented and trusted**
4) can potentially be influenced by product changes (actionable)

A **non-signal** is:
- a metric that happens **after** conversion (label leakage)
- a proxy that is mostly driven by marketing attribution quirks
- a variable that changes meaning across platforms/markets
- something we cannot realistically influence

---

## 2) Guardrails (what we will NOT allow)
### 2.1 Label leakage (hard rule)
We will not include anything that directly encodes “paid subscription” or the purchase funnel completion, for example:
- payment_success, subscription_active, plan_changed_to_paid
- receipt validation events
- post-purchase entitlements
- “premium_content_played” if it requires already being premium

### 2.2 Post-treatment bias
If a metric is affected by an experiment or intervention we are evaluating, we must treat it carefully.
Example: if we change onboarding, onboarding completion may become “treatment-dependent”.

### 2.3 Non-comparable definitions
Signals must be consistent across:
- platform (iOS/Android/Web)
- geography (MX/US/etc)
- app versions
If not, we either normalize or exclude.

---

## 3) Time windows (so signals are comparable)
We will define signals within a **fixed observation window** relative to a common anchor event.

**Anchor event (example):** `account_created` or `first_app_open`

**Candidate observation windows:**
- **D0 (first session)**: first 0–60 minutes
- **D1**: first 24 hours
- **D7**: first 7 days

We will start with **D7** as the main window (more behavior captured), and use D0/D1 for sensitivity checks.

---

## 4) Candidate signal taxonomy
Below is a product-first taxonomy. Final selection will be driven by data availability and reliability.

### A) Activation signals (early value realization)
These indicate the user experienced “aha” moments.
- first_content_play
- first_download_completed (if relevant to the product)
- number_of_distinct_days_active (within window)
- session_count / total_listening_minutes

**Why it could matter:** users who reach value faster are more likely to pay.

---

### B) Engagement depth signals (habit strength)
- total_active_days
- content diversity (unique artists/genres)
- repeat behavior (plays per day)
- streak proxy (active consecutive days)

**Why it could matter:** deeper habit → higher perceived value → higher willingness to pay.

---

### C) Intent signals (purchase curiosity)
- paywall_view_count
- pricing_page_visit
- plan_picker_view
- subscription_cta_click (without completion)

**Why it could matter:** explicit curiosity about premium.

---

### D) Friction / pain signals (drivers of upgrade)
These show the user hit limits or annoyance.
- ad_impressions / ad_exposure_minutes (if applicable)
- interrupted_sessions (e.g., buffering, errors)
- download_wait_time_events (if applicable)
- “feature_blocked” events (if premium gates exist)

**Why it could matter:** users upgrade when friction is high *and* value is proven.

---

### E) Trust & quality signals (risk reducers)
- email_verified
- successful_payment_method_add (without purchase)
- crash_free_sessions proxy (or app stability proxy)
- support_contact / help_center_visit

**Why it could matter:** higher trust reduces drop-off at the moment of payment.

---

## 5) Signal quality checklist (must pass)
Each candidate signal should pass this checklist:

1) **Definition**
- exact event(s)
- computation method (count/sum/binary)
- unit (per user per window)

2) **Coverage**
- % of users with non-null values
- platform coverage

3) **Stability**
- distribution is not wildly different week to week
- not driven by tracking bugs

4) **Directionality**
- expected relationship with conversion (hypothesis)

5) **Actionability**
- what product lever could move it?

---

## 6) Minimal feature set (first modeling pass)
We will start with a small, interpretable set (10–20 signals max) that covers:
- activation
- engagement
- intent
- friction

This keeps the first model readable and prevents “feature soup”.

---

## 7) Output of this phase
At the end of Phase 3, we will publish:
- `signals_catalog.md` (final definitions + formulas)
- a short table of selected signals (name, type, expected direction, notes)
- explicit exclusions (leakage / unreliable / non-actionable)

---

## Next: Phase 4 — Modeling & insights
Once signals are defined and validated, we can model:
- conversion likelihood (interpretable baseline)
- segmentation by signal patterns
- which signals are strongest and most actionable
- product recommendations tied to signal movement
