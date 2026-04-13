risk_score = severity_weight * domain_weight

if risk_score >= 20:
    decision = "STOP"
    primary_reason = "High risk score in critical domain"
    recommended_action = "Block deployment pending investigation"
elif risk_score >= 12:
    decision = "CAUTION"
    primary_reason = "Elevated risk requiring human review"
    recommended_action = "Require explicit human approval"
else:
    decision = "GO"
    primary_reason = "Low risk score"
    recommended_action = "Proceed with deployment"

decision_result = {
    "decision": decision,
    "risk_score": risk_score,
    "signals": {
        "severity_weight": severity_weight,
        "domain_weight": domain_weight
    },
    "primary_reason": primary_reason,
    "recommended_action": recommended_action
}
