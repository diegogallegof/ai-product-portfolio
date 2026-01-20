# Success Metrics and Risks

This document defines how the success of the proposed recommendations
would be measured and how potential risks would be identified and managed.

The objective is to ensure that decisions are evaluated holistically,
balancing conversion gains with user experience and long-term product health.

---

## 1) Measurement principles

All metrics are selected according to the following principles:

1. **Decision relevance**  
   Metrics must inform whether to scale, iterate, or stop an initiative.

2. **Primary vs secondary separation**  
   Primary metrics determine success; secondary metrics monitor side effects.

3. **Leading and lagging indicators**  
   Early signals are monitored alongside longer-term outcomes.

4. **Segment-aware evaluation**  
   Results are interpreted by cohort, not only in aggregate.

---

## 2) Primary success metrics

These metrics determine whether a recommendation is successful.

### 2.1 Subscription conversion rate
- Core business KPI
- Measured by cohort and experiment variant
- Evaluated as absolute lift and relative change

### 2.2 Payment completion rate
- Especially relevant for friction-reduction initiatives
- Indicates effectiveness of checkout improvements

### 2.3 Revenue per exposed user
- Guards against monetization strategies that increase conversion
  but reduce overall revenue quality

---

## 3) Secondary and guardrail metrics

These metrics detect unintended consequences.

### 3.1 Engagement health
- Core engagement frequency
- Session depth or completion of key actions

Purpose:
- Ensure monetization does not suppress product usage

---

### 3.2 Retention indicators
- Short-term retention (D7 / D14)
- Return behavior after monetization exposure

Purpose:
- Detect early signs of churn or dissatisfaction

---

### 3.3 User fatigue signals
- Declining interaction rates with monetization surfaces
- Increased dismissals or avoidance behavior

Purpose:
- Identify overexposure or poor sequencing effects

---

### 3.4 Support and friction signals
- Checkout error frequency
- Help-seeking or support contact events

Purpose:
- Catch technical or UX regressions early

---

## 4) Risk categories and mitigation strategies

### 4.1 Monetization fatigue risk

**Description:**  
Overexposure to paywalls or prompts may reduce user trust.

**Mitigation:**  
- Frequency caps
- Context-aware exposure rules
- Monitoring of fatigue signals

---

### 4.2 Conversion cannibalization risk

**Description:**  
Delaying monetization may reduce short-term revenue.

**Mitigation:**  
- Cohort-based revenue tracking
- Time-to-conversion analysis

---

### 4.3 Segment misalignment risk

**Description:**  
A recommendation may work for some segments but harm others.

**Mitigation:**  
- Segment-level analysis
- Progressive rollout by cohort

---

### 4.4 Measurement bias risk

**Description:**  
Instrumentation gaps or cohort leakage may distort results.

**Mitigation:**  
- Metric definition audits
- Consistent experiment enrollment rules

---

## 5) Early warning signals

The following signals trigger review or rollback:

- Sharp drop in engagement or retention
- Increase in checkout error rates
- Significant negative impact in a specific segment
- Divergence between conversion lift and revenue quality

Early detection enables rapid iteration without long-term damage.

---

## 6) Decision thresholds

Recommendations are evaluated against predefined thresholds:

- **Scale:** Sustained positive lift with no major guardrail violations
- **Iterate:** Mixed results or segment-specific effects
- **Stop:** No lift or unacceptable negative impact

These thresholds ensure disciplined decision-making.

---

## 7) Summary

Success is defined not only by higher conversion,
but by **sustainable monetization aligned with user value**.

Clear metrics and explicit risk management
enable confident decisions under uncertainty
and protect long-term product health.

This document concludes **Phase 5: Product Recommendations**.
