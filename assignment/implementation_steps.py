"""
Step-by-step implementation checklist in Python form.
Replace TODOs with real code in the student's project.
"""

STEP_1 = "Open starter_project/ and review dags/, src/, data/, expected/, and scripts/."
STEP_2 = "Confirm orders_failed.csv and orders_passed.csv exist in starter_project/data/."
STEP_3 = "Complete src/config.py with valid statuses, input path, output path, and webhook settings."
STEP_4 = "Complete src/validation.py so it reads CSV rows with csv.DictReader."
STEP_5 = "Count invalid rows for customer_id, amount, and status."
STEP_6 = "Build a summary dictionary and save it as JSON."
STEP_7 = "Send the summary to Discord."
STEP_8 = "Raise an exception when validation_status == 'failed'."
STEP_9 = "Connect the validation function to dags/sales_data_quality_pipeline.py."
STEP_10 = "Run starter_project/scripts/run_local_check.py with both datasets."
STEP_11 = "Compare generated output with starter_project/expected/."
STEP_12 = "Use a mock webhook first if the real Discord webhook is not stable."


def implementation_checklist() -> list[str]:
    return [
        STEP_1,
        STEP_2,
        STEP_3,
        STEP_4,
        STEP_5,
        STEP_6,
        STEP_7,
        STEP_8,
        STEP_9,
        STEP_10,
        STEP_11,
        STEP_12,
    ]


def print_checklist() -> None:
    for index, step in enumerate(implementation_checklist(), start=1):
        print(f"{index}. {step}")


if __name__ == "__main__":
    print_checklist()
