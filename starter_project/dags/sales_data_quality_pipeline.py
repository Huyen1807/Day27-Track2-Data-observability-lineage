from __future__ import annotations

from datetime import datetime
from pathlib import Path
import sys

try:
    from airflow import DAG
    from airflow.operators.python import PythonOperator
except ImportError:  # pragma: no cover
    DAG = None

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))


def validate_orders_task() -> dict:
    # 1. Import config values and validation functions
    from src.config import AIRFLOW_INPUT_FILE, SUMMARY_FILE
    from src.validation import (
        read_rows,
        build_summary,
        write_summary,
        send_discord_message,
        LabValidationError,
    )

    # 2. Read the input CSV.
    print(f"Reading data from {AIRFLOW_INPUT_FILE}...")
    rows = read_rows(AIRFLOW_INPUT_FILE)

    # 3. Validate the rows.
    summary = build_summary(rows)
    print(f"Validation summary: {summary}")

    # 4. Write the JSON summary.
    write_summary(summary, SUMMARY_FILE)
    print(f"Summary written to {SUMMARY_FILE}")

    # 5. Send the Discord alert.
    send_discord_message(summary)
    print("Discord notification sent.")

    # 6. Raise an error on failed validation.
    if summary["validation_status"] == "failed":
        raise LabValidationError(f"Data validation failed! {summary}")

    return summary


if DAG is not None:
    with DAG(
        dag_id="sales_data_quality_pipeline",
        start_date=datetime(2024, 1, 1),
        schedule=None,
        catchup=False,
        tags=["lab", "data-quality", "discord"],
    ) as dag:
        validate_orders = PythonOperator(
            task_id="validate_orders",
            python_callable=validate_orders_task,
        )
else:  # pragma: no cover
    dag = None
