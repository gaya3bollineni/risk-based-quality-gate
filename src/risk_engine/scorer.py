from typing import List
from risk_engine.models import TestResult

SEVERITY_WEIGHTS = {
    "LOW": 5,
    "MEDIUM": 10,
    "HIGH": 20,
    "CRITICAL": 40,
}

AREA_WEIGHTS = {
    "auth": 15,
    "payments": 30,
    "claims": 35,
    "reporting": 10,
}

def score_release(results: List[TestResult]):
    # Calculates an overall release risk score based on failed tests.

    total_score = 0

    for test in results:
        if test.status != "FAIL":
            continue

        severity_score = SEVERITY_WEIGHTS.get(test.severity.upper(), 10)
        area_score = AREA_WEIGHTS.get(test.area.lower(), 10)

        total_score += severity_score + area_score

    if total_score >= 60:
        decision = "STOP"
        primary_reason = "High aggregated risk score across critical areas"
        recommended_action = "Block deployment pending investigation"
    elif total_score >= 30:
        decision = "CAUTION"
        primary_reason = "Elevated risk score requiring human review"
        recommended_action = "Require explicit human approval"
    else:
        decision = "GO"
        primary_reason = "Low aggregated risk score"
        recommended_action = "Proceed with deployment"

    explanation = {
        "primary_reason": primary_reason,
        "recommended_action": recommended_action
    }

    return total_score, decision, explanation