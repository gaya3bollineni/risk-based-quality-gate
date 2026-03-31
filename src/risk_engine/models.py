from dataclasses import dataclass

@dataclass
class TestResult:
    
   # Represents a single test outcome with contextual risk information.
    
    name: str
    status: str      # PASS or FAIL
    severity: str    # LOW, MEDIUM, HIGH, CRITICAL
    area: str        # business domain (e.g., claims, payments, auth)
