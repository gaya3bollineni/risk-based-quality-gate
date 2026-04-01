# Risk Scoring and Release Decisions

This project evaluates release readiness by interpreting test failures in context rather than treating all failures equally.

## Inputs Considered

Each test result provides the following information:

- **Execution status** (PASS or FAIL)
- **Severity level** (LOW, MEDIUM, HIGH, CRITICAL)
- **Business domain** (e.g., claims, payments, authentication)

## Scoring Approach

Release risk is calculated by combining:

- A severity weight
- A domain impact weight

Failures in high-impact business areas and with higher severity contribute more to the overall risk score.

## Decision Thresholds

The cumulative risk score maps to one of three release outcomes:

- **GO** — Risk is low and understood
- **CAUTION** — Elevated risk; review recommended
- **STOP** — High risk; release should be blocked

## Design Philosophy

This logic mirrors how experienced engineers reason about release readiness in enterprise systems.

The goal is explainability and decision support, not prediction or automation of judgment.
