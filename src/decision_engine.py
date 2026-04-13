risk_score = severity_weight * domain_weight

if risk_score >= 20:
    decision = "STOP"
elif risk_score >= 12:
    decision = "CAUTION"
else:
    decision = "GO"
