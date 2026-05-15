"""
Student-facing assignment brief.
"""

LAB_NAME = "sales_data_quality_pipeline"
PROJECT_FOLDER = "starter_project"

OBJECTIVE = """
Build an Apache Airflow DAG that:
1. Reads a sales orders CSV file from starter_project/data/.
2. Validates customer_id, amount, and status.
3. Writes output/validation_summary.json automatically.
4. Sends a Discord webhook message.
5. Raises an exception when validation fails.
""".strip()

READINESS_NOTES = {
    "lab_package": "ready",
    "local_validation": "ready",
    "reference_airflow_run": "verified",
    "real_discord_delivery": "depends on a valid webhook",
}

VALIDATION_RULES = {
    "customer_id": "must not be empty",
    "amount": "must be numeric and > 0",
    "status": "must be one of: completed, pending, cancelled",
}

EXPECTED_FAILED_SUMMARY = {
    "row_count": 10,
    "missing_customer_ids": 2,
    "invalid_amounts": 2,
    "invalid_statuses": 2,
    "validation_status": "failed",
}

EXPECTED_PASSED_SUMMARY = {
    "row_count": 10,
    "missing_customer_ids": 0,
    "invalid_amounts": 0,
    "invalid_statuses": 0,
    "validation_status": "passed",
}


def print_lab_brief() -> None:
    print(f"Lab: {LAB_NAME}")
    print(f"Starter project folder: {PROJECT_FOLDER}")
    print(OBJECTIVE)
    print("\nValidation rules:")
    for field_name, rule in VALIDATION_RULES.items():
        print(f"- {field_name}: {rule}")
    print("\nExpected failed summary:")
    print(EXPECTED_FAILED_SUMMARY)
    print("\nExpected passed summary:")
    print(EXPECTED_PASSED_SUMMARY)
    print("\nReadiness notes:")
    print(READINESS_NOTES)


if __name__ == "__main__":
    print_lab_brief()
