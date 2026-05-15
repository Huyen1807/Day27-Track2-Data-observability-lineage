# Sales Data Quality Lab

This repository is structured as a professional lab-assignment package for an Apache Airflow data-quality exercise. Students are expected to build a small pipeline that validates sales order data, writes a JSON validation summary, and sends a Discord notification.

## Assignment Summary

Students must work with two input datasets:

- a mock dataset that intentionally fails validation
- a clean dataset that passes validation

Students do not manually create the validation summary JSON. The DAG must generate `validation_summary.json` automatically after reading the input CSV.

## Package Layout

```text
labs/
├── assignment/
│   ├── implementation_steps.py
│   ├── lab_brief.py
│   └── pseudocode.py
├── grading/
│   └── rubric.md
└── starter_project/
    ├── dags/
    │   └── sales_data_quality_pipeline.py
    ├── data/
    │   ├── orders_failed.csv
    │   └── orders_passed.csv
    ├── expected/
    │   ├── validation_summary_failed.json
    │   └── validation_summary_passed.json
    ├── scripts/
    │   └── run_local_check.py
    └── src/
        ├── __init__.py
        ├── config.py
        └── validation.py
```

## What Each Folder Is For

- `assignment/`: student-facing assignment brief, implementation checklist, and Python-style pseudocode
- `starter_project/`: the clean starter project students can run and extend
- `grading/`: scoring rubric for instructors or TAs

## Learning Outcomes

- Build an Airflow DAG with Python tasks
- Validate CSV data with simple business rules
- Generate a JSON summary file automatically
- Fail the pipeline when bad data is detected
- Send operational notifications to Discord

## Required Student Deliverables

- `starter_project/dags/sales_data_quality_pipeline.py`
- completed logic in `starter_project/src/config.py`
- completed logic in `starter_project/src/validation.py`
- two CSV datasets in `starter_project/data/`
- generated `starter_project/output/validation_summary.json`
- a success Discord notification for the passing dataset
- a failure Discord notification for the failing dataset

## Validation Rules

1. `customer_id` must not be empty.
2. `amount` must be numeric and greater than `0`.
3. `status` must be one of `completed`, `pending`, or `cancelled`.

## Dataset Requirements

### Failing Dataset

Purpose:
- confirm the Airflow pipeline stops when validation fails
- confirm the pipeline sends a Discord failure alert

Required file:
- `starter_project/data/orders_failed.csv`

Expected failure patterns:
- at least one row with a missing `customer_id`
- at least one row with an `amount <= 0`
- at least one row with an invalid `status`

Current starter dataset:
- [starter_project/data/orders_failed.csv](/Users/duongnh59.al1/Documents/Project/Vin20K/Day27-Track2-v2/labs/starter_project/data/orders_failed.csv)

Expected generated summary:
- [starter_project/expected/validation_summary_failed.json](/Users/duongnh59.al1/Documents/Project/Vin20K/Day27-Track2-v2/labs/starter_project/expected/validation_summary_failed.json)

### Passing Dataset

Purpose:
- confirm the Airflow pipeline continues successfully
- confirm the pipeline sends a Discord success alert

Required file:
- `starter_project/data/orders_passed.csv`

Expected passing rules:
- no missing `customer_id`
- all `amount` values are greater than `0`
- all `status` values are valid

Current starter dataset:
- [starter_project/data/orders_passed.csv](/Users/duongnh59.al1/Documents/Project/Vin20K/Day27-Track2-v2/labs/starter_project/data/orders_passed.csv)

Expected generated summary:
- [starter_project/expected/validation_summary_passed.json](/Users/duongnh59.al1/Documents/Project/Vin20K/Day27-Track2-v2/labs/starter_project/expected/validation_summary_passed.json)

## Student Entry Points

- [assignment/lab_brief.py](/Users/duongnh59.al1/Documents/Project/Vin20K/Day27-Track2-v2/labs/assignment/lab_brief.py)
- [assignment/implementation_steps.py](/Users/duongnh59.al1/Documents/Project/Vin20K/Day27-Track2-v2/labs/assignment/implementation_steps.py)
- [assignment/pseudocode.py](/Users/duongnh59.al1/Documents/Project/Vin20K/Day27-Track2-v2/labs/assignment/pseudocode.py)
- [starter_project/dags/sales_data_quality_pipeline.py](/Users/duongnh59.al1/Documents/Project/Vin20K/Day27-Track2-v2/labs/starter_project/dags/sales_data_quality_pipeline.py)
- [starter_project/src/config.py](/Users/duongnh59.al1/Documents/Project/Vin20K/Day27-Track2-v2/labs/starter_project/src/config.py)
- [starter_project/src/validation.py](/Users/duongnh59.al1/Documents/Project/Vin20K/Day27-Track2-v2/labs/starter_project/src/validation.py)
- [starter_project/scripts/run_local_check.py](/Users/duongnh59.al1/Documents/Project/Vin20K/Day27-Track2-v2/labs/starter_project/scripts/run_local_check.py)
- [grading/rubric.md](/Users/duongnh59.al1/Documents/Project/Vin20K/Day27-Track2-v2/labs/grading/rubric.md)

## Quick Run

```bash
python3 starter_project/scripts/run_local_check.py starter_project/data/orders_passed.csv --skip-discord
python3 starter_project/scripts/run_local_check.py starter_project/data/orders_failed.csv --allow-failure --skip-discord
```

## Expected Pipeline Behavior

When `orders_passed.csv` is used:
- the validation task succeeds
- `validation_summary.json` is generated
- the summary reports zero validation errors
- a success notification is sent to Discord

When `orders_failed.csv` is used:
- the validation task writes `validation_summary.json`
- the summary reports validation failures
- a failure notification is sent to Discord
- the pipeline stops after validation failure

## Expected Summary Shape

The DAG-generated JSON must include:

```json
{
  "row_count": 0,
  "missing_customer_ids": 0,
  "invalid_amounts": 0,
  "invalid_statuses": 0,
  "validation_status": "passed_or_failed"
}
```

## Recommended Airflow Project Layout

```text
airflow_project/
├── dags/
│   └── sales_data_quality_pipeline.py
├── data/
│   ├── orders_failed.csv
│   └── orders_passed.csv
└── output/
    └── validation_summary.json
```

## Verification Notes

- The starter package has been checked locally with both datasets.
- The reference implementation has been executed in Airflow.
- The Discord code path works, but the real webhook must be valid to receive production messages.

## Readiness

- Assignment package: ready
- Starter project structure: ready
- Local validation flow: ready
- Reference Airflow logic: verified separately
- Real Discord delivery: depends on a valid webhook URL
