from __future__ import annotations


PROJECT_ROOT = "starter_project"
VALID_STATUSES = {"completed", "pending", "cancelled"}


def validate_orders_pseudocode(input_csv_path: str, output_json_path: str, webhook_url: str) -> dict:
    """
    Python-style pseudocode for the student solution.
    This file is intentionally close to real code, but still leaves implementation details open.
    """

    rows = read_csv_rows(input_csv_path)  # e.g. starter_project/data/orders_passed.csv

    missing_customer_ids = 0
    invalid_amounts = 0
    invalid_statuses = 0

    for row in rows:
        customer_id = row["customer_id"].strip()
        amount = row["amount"].strip()
        status = row["status"].strip()

        if not customer_id:
            missing_customer_ids += 1

        if not is_positive_number(amount):  # TODO: implement numeric check
            invalid_amounts += 1

        if status not in VALID_STATUSES:
            invalid_statuses += 1

    summary = {
        "row_count": len(rows),
        "missing_customer_ids": missing_customer_ids,
        "invalid_amounts": invalid_amounts,
        "invalid_statuses": invalid_statuses,
        "validation_status": "passed",
    }

    if missing_customer_ids or invalid_amounts or invalid_statuses:
        summary["validation_status"] = "failed"

    write_summary_json(output_json_path, summary)  # e.g. starter_project/output/validation_summary.json
    send_discord_message(webhook_url, summary)

    if summary["validation_status"] == "failed":
        raise ValueError("Validation failed. Stop the pipeline.")

    return summary


def read_csv_rows(input_csv_path: str) -> list[dict]:
    raise NotImplementedError


def is_positive_number(raw_amount: str) -> bool:
    raise NotImplementedError


def write_summary_json(output_json_path: str, summary: dict) -> None:
    raise NotImplementedError


def send_discord_message(webhook_url: str, summary: dict) -> None:
    raise NotImplementedError
