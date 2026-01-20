# Recommendation Set

This document presents a **small, prioritized set of product recommendations**
derived from validated insights and evaluated using the decision framework
defined in this phase.

The recommendations focus on **maximizing subscription conversion**
while managing risk, execution complexity, and long-term product health.

---

## Overview

Rather than proposing a broad list of ideas,
this case study intentionally limits recommendations to a **focused set of high-leverage actions**.

Each recommendation includes:
- The insight(s) that support it
- The concrete product action
- The target user segment
- Expected impact and confidence
- Key trade-offs and risks

---

## Recommendation 1 — Sequence monetization after early value realization

### Insight basis
- Early activation and repeated core engagement are strong prerequisites for conversion
- Monetization prompts shown before value realization show weak or negative lift

### Recommendation
Delay premium paywall exposure until users have demonstrated
at least one **clear value realization signal** (e.g., successful core action completion).

### Target segment
- New users in their first 7 days
- Users who have not yet completed an activation milestone

### Expected impact
- **Impact:** High  
- **Confidence:** High  
- **Execution complexity:** Medium  
- **Risk:** Low

### Trade-offs
- Potential short-term revenue delay
- Requires clear definition of “value realized”

---

## Recommendation 2 — Prioritize mid-early intent signals for intervention (D3–D7)

### Insight basis
- Prediction accuracy improves over time, but actionability declines
- The majority of meaningful intervention opportunity exists by Day 7

### Recommendation
Focus conversion interventions (messaging, offers, nudges)
around **D3–D7 windows**, rather than immediate onboarding or late-stage pushes.

### Target segment
- Users with activation signals but no payment attempt
- Users showing increasing engagement momentum

### Expected impact
- **Impact:** Medium–High  
- **Confidence:** Medium  
- **Execution complexity:** Low  
- **Risk:** Low

### Trade-offs
- Slightly weaker predictive confidence than late-stage signals
- Requires lifecycle-aware orchestration

---

## Recommendation 3 — Cap monetization exposure to avoid saturation effects

### Insight basis
- Conversion likelihood increases with monetization exposure up to a point
- Excessive paywall impressions correlate with lower conversion and higher fatigue

### Recommendation
Introduce frequency caps and contextual rules
for monetization surfaces to prevent overexposure.

### Target segment
- Highly engaged non-converting users
- Users repeatedly encountering paywalls without action

### Expected impact
- **Impact:** Medium  
- **Confidence:** Medium  
- **Execution complexity:** Low  
- **Risk:** Low–Medium

### Trade-offs
- Requires tuning to avoid under-monetization
- Short-term conversion rate may fluctuate during adjustment

---

## Recommendation 4 — Treat friction reduction as a primary conversion lever

### Insight basis
- Checkout errors and failed payment attempts sharply suppress conversion
- Friction effects dominate even in the presence of strong intent signals

### Recommendation
Prioritize reduction of payment and checkout friction
before introducing additional monetization messaging or incentives.

### Target segment
- Users who initiate but fail payment flows
- High-intent users encountering technical errors

### Expected impact
- **Impact:** High  
- **Confidence:** High  
- **Execution complexity:** Medium  
- **Risk:** Low

### Trade-offs
- Engineering-heavy compared to messaging changes
- Less visible than new monetization features

---

## Recommendation 5 — Use intent signals to personalize, not intensify, monetization

### Insight basis
- Intent signals are meaningful only when combined with prior activation
- Aggressive monetization without personalization leads to diminishing returns

### Recommendation
Use intent signals to **personalize timing, messaging, and surface choice**
rather than increasing overall monetization pressure.

### Target segment
- Activated users with emerging intent signals
- Users with prior exposure but no conversion

### Expected impact
- **Impact:** Medium  
- **Confidence:** Medium  
- **Execution complexity:** Medium  
- **Risk:** Medium

### Trade-offs
- Requires coordination across product, data, and UX
- Higher complexity than static rules

---

## Summary

These recommendations intentionally prioritize:
- Fewer, higher-confidence actions
- Early but actionable intervention points
- Long-term conversion health over short-term pressure

All recommendations are designed to be:
- Testable
- Reversible
- Incrementally deployable

They form the basis for the **experiment design** detailed in the next document.
