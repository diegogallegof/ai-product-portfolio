# Signals Catalog (Subscription Conversion)

This catalog defines the behavioral signals considered for the **User Conversion Case Study**.

Signals here are not “features for a model” by default.  
They are **decision signals**: observable behaviors that can help a product team understand *why conversion is flat* and *where to intervene*.

All signals will be evaluated using the framework defined in:
- `03_signal_definition/signal_evaluation_plan.md`

---

## 1) Signal selection criteria (quick reference)

Each signal is assessed on three dimensions:

- **Predictive value** — Does it correlate with conversion?
- **Stability** — Does it behave consistently over time and cohorts?
- **Actionability** — Can a product team realistically influence it?

---

## 2) Catalog format

For each signal we capture:

- **Signal name**
- **Definition**
- **Why it matters (product intuition)**
- **How to compute**
- **Expected direction**
- **Evaluation notes**
- **Caveats / risks**
- **Action levers (what product can do)**

---

## 3) Signals catalog

### A) Activation & early value signals

#### A1. Day-0 activation completed
- **Definition:** User completes the activation milestone within first session (e.g., completes onboarding + performs first “core action”).
- **Why it matters:** If users don’t reach early value, conversion messaging won’t matter.
- **How to compute:** `activation_event = 1` if user triggers activation milestone within `t <= 24h` of first_seen.
- **Expected direction:** Higher activation → higher conversion likelihood.
- **Evaluation notes:** Compare conversion rates by activation status and time-to-activation buckets.
- **Caveats:** Activation definition must match the product’s real value moment, not a vanity event.
- **Action levers:** Reduce onboarding friction, shorten time-to-first-value, improve guided flows.

#### A2. Time to first value (TTFV)
- **Definition:** Time from first_seen to first meaningful value event.
- **Why it matters:** Faster value tends to increase intent and reduce churn before paywall.
- **How to compute:** `TTFV = timestamp(first_value_event) - timestamp(first_seen)`.
- **Expected direction:** Lower TTFV → higher conversion.
- **Evaluation notes:** Use percentiles; look for sharp drop-offs after thresholds (e.g., >10 min).
- **Caveats:** Ensure “first value” is truly value (not just browsing).
- **Action levers:** UX clarity, defaults, recommendations, reduce waiting/failure states.

---

### B) Engagement depth signals

#### B1. Core actions per day (first 7 days)
- **Definition:** Count of core product actions per day during days 0–6.
- **Why it matters:** Sustained engagement indicates habit formation and higher willingness to pay.
- **How to compute:** `core_actions_7d = sum(core_action_events) within first 7 days`.
- **Expected direction:** Higher engagement → higher conversion.
- **Evaluation notes:** Check diminishing returns (is 10 actions meaningfully better than 5?).
- **Caveats:** High counts can be driven by friction loops (retries/errors).
- **Action levers:** Improve discovery loops, reduce dead ends, better content/feature surfacing.

#### B2. Session frequency (first 7 days)
- **Definition:** Number of distinct sessions in first 7 days.
- **Why it matters:** More sessions = repeated intent signals, not just one-time curiosity.
- **How to compute:** `sessions_7d` via sessionization logic.
- **Expected direction:** Higher → higher conversion.
- **Evaluation notes:** Segment by acquisition source if available.
- **Caveats:** Session definition must be consistent (timeout window).
- **Action levers:** Reminders, lifecycle nudges, streaks, save/resume experiences.

---

### C) Intent & paywall proximity signals

#### C1. Premium page visits
- **Definition:** User visits pricing/premium page (or equivalent) within first 14 days.
- **Why it matters:** Strong explicit intent; often a top predictor.
- **How to compute:** `premium_page_visit = 1` if event occurs within 14d.
- **Expected direction:** Visit → higher conversion probability.
- **Evaluation notes:** Also measure **time from first_seen to first premium page visit**.
- **Caveats:** Visits can be forced by UX (gating), not user intent.
- **Action levers:** Improve premium positioning, clarify benefits, contextual prompts.

#### C2. Paywall impressions
- **Definition:** User sees paywall N times in first 14 days.
- **Why it matters:** Measures exposure to monetization surface.
- **How to compute:** `paywall_impressions_14d = count(paywall_shown)` within 14d.
- **Expected direction:** Non-linear (too few = low awareness; too many = frustration).
- **Evaluation notes:** Look for optimal range; test interaction with engagement segments.
- **Caveats:** Can be confounded by product gating design and user paths.
- **Action levers:** Adjust entry points, caps, sequencing, personalization.

#### C3. Payment start event
- **Definition:** User initiates checkout / payment flow.
- **Why it matters:** Closest pre-conversion intent; separates “considering” from “acting”.
- **How to compute:** `payment_start = 1` if event fired.
- **Expected direction:** Strong positive relationship with conversion.
- **Evaluation notes:** Analyze drop-off to payment_complete by platform/payment method.
- **Caveats:** Can include accidental taps; validate with dwell time or subsequent steps.
- **Action levers:** Reduce checkout friction, clarify pricing, fix errors, trust signals.

---

### D) Trust & friction signals

#### D1. Checkout errors / failed payment attempts
- **Definition:** Number of payment failures or checkout errors during payment flow.
- **Why it matters:** High friction directly blocks conversion (involuntary non-conversion).
- **How to compute:** `checkout_error_count` during payment funnel window.
- **Expected direction:** Higher errors → lower conversion (strong negative).
- **Evaluation notes:** Break down by error type and platform.
- **Caveats:** Logging quality matters; ensure error taxonomy is accurate.
- **Action levers:** Error messaging, retries, alternate payment methods, local payment options.

#### D2. Support/help intent during paywall or checkout
- **Definition:** User opens FAQ/help, “restore purchase”, or support links near payment.
- **Why it matters:** Proxy for uncertainty, trust gaps, or confusion.
- **How to compute:** Count help/support events within ±10 min of paywall/checkout events.
- **Expected direction:** Often negative, but can be positive if it resolves and converts.
- **Evaluation notes:** Check conditional effect: “help opened + successful conversion”.
- **Caveats:** Some users are careful; interpret with context.
- **Action levers:** Improve clarity, add trust badges, simplify wording, localized FAQs.

---

## 4) Prioritization (initial)

This is an initial prioritization before quantitative evaluation:

**Tier 1 (high intent / close to conversion)**
- Premium page visits
- Paywall impressions (optimal range)
- Payment start

**Tier 2 (engagement & value formation)**
- Day-0 activation
- Time to first value
- Core actions per day
- Session frequency

**Tier 3 (friction & trust)**
- Checkout errors
- Help/support intent near checkout

---

## 5) Next steps

1. Validate event definitions and time windows.
2. Run signal evaluation:
   - Predictive value
   - Stability across cohorts/time
   - Actionability mapping
3. Select a final signal set for Phase 4 (Modeling & insights).
