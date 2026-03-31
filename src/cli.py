import json
import sys
from risk_engine.models import TestResult
from risk_engine.scorer import score_release

def load_test_results(path):
    
    #Loads test results from a JSON file and converts them into TestResult objects.
    
    with open(path, "r") as file:
        raw_data = json.load(file)

    results = []
    for item in raw_data:
        results.append(
            TestResult(
                name=item["name"],
                status=item["status"],
                severity=item["severity"],
                area=item["area"],
            )
        )
    return results


def main():
    if len(sys.argv) < 2:
        print("Usage: python src/cli.py <path_to_test_results.json>")
        sys.exit(1)

    file_path = sys.argv[1]
    test_results = load_test_results(file_path)

    score, decision = score_release(test_results)

    print(f"Release Risk Score: {score}")
    print(f"Decision: {decision}")

    # Exit with non‑zero status if risk is too high
    if decision == "STOP":
        sys.exit(1)


if __name__ == "__main__":
    main()
