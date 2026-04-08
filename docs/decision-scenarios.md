# Risk-Based Quality Gate: Decision Scenarios

This document illustrates how the risk-based quality gate behaves
in realistic CI/CD pipeline situations.

The goal is to show decision reasoning — not test execution.

---

## Scenario 1: Multiple Low-Risk Test Failures

**Context**
- UI-related tests fail in a non-critical reporting module
- Core business logic tests pass

**Signals**
- Failed tests: 5
- Severity: Low
- Domain criticality: Low

**Reasoning**
- Failures do not impact core workflows or compliance
- Risk surface is limited to presentation layer

**Decision**
✅ **GO**

The pipeline proceeds with deployment.

---

## Scenario 2: Single High-Risk Failure in Critical Domain

**Context**
- All tests pass except one payment validation test
- The failure affects financial transaction logic

**Signals**
- Failed tests: 1
- Severity: High
- Domain criticality: High

**Reasoning**
- Even a single failure in a critical domain carries high business risk
- Failure could lead to incorrect billing or regulatory exposure

**Decision**
🛑 **STOP**

Deployment is blocked pending investigation.

---

## Scenario 3: Mixed Severity with Uncertain Risk

**Context**
- One high-severity test failure in a rarely used feature
- Several medium-severity failures in adjacent components

**Signals**
- Failed tests: 3
- Severity: Mixed
- Domain criticality: Medium

**Reasoning**
- Impact is unclear without human review
- Automated decision would be unsafe either way

**Decision**
⚠️ **CAUTION**

Deployment requires explicit human approval.
