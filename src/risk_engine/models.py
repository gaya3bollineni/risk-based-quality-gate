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
    elif total_score >= 30:
        decision = "CAUTION"
    else:
        decision = "GO"

    return total_score, decision
