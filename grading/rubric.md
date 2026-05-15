# Scoring Rubric

Total: 10 points

## Grading Guidance

The student submission should be checked with both datasets:

- `starter_project/data/orders_passed.csv`
- `starter_project/data/orders_failed.csv`

The student should not hand-write `validation_summary.json`. That file must be created automatically by the DAG or validation logic.

## 1. DAG Structure And Execution - 2 points

- 2: DAG is valid, named correctly, and can be triggered manually.
- 1: DAG exists but has minor configuration issues.
- 0: DAG missing or unusable.

Evidence to check:

- DAG name is `sales_data_quality_pipeline`
- Airflow can discover the DAG
- DAG can be run against the provided datasets

## 2. CSV Ingestion And Dataset Handling - 2 points

- 2: Reads the input CSV correctly and handles all rows.
- 1: Reads data partially or with small mistakes.
- 0: Cannot read the dataset.

Evidence to check:

- `orders_failed.csv` is present
- `orders_passed.csv` is present
- the code reads `order_id`, `customer_id`, `amount`, and `status`

## 3. Validation Logic - 3 points

- 3: Correctly checks missing `customer_id`, invalid `amount`, and invalid `status`.
- 2: Two rules work correctly.
- 1: One rule works correctly.
- 0: Validation is incorrect or missing.

Evidence to check:

- failing dataset produces non-zero counts
- passing dataset produces zero counts
- status validation only allows `completed`, `pending`, and `cancelled`

## 4. Output JSON - 1 point

- 1: Generates `validation_summary.json` with the correct counts and status.
- 0: Output file missing or incorrect.

Evidence to check:

- JSON file is created automatically
- JSON contains `row_count`
- JSON contains `missing_customer_ids`
- JSON contains `invalid_amounts`
- JSON contains `invalid_statuses`
- JSON contains `validation_status`

## 5. Discord Alert - 1 point

- 1: Sends a meaningful success/failure alert through the webhook.
- 0: Alert missing or broken.

Evidence to check:

- passing dataset triggers a success alert
- failing dataset triggers a failure alert
- alert content identifies the dataset or validation result clearly

## 6. Failure Handling - 1 point

- 1: Pipeline stops when validation fails and still preserves the summary file.
- 0: Pipeline continues incorrectly or loses the failure summary.

Evidence to check:

- failed dataset causes the validation path to raise an error or fail the task
- summary file still exists after failure

## Expected Outputs

Minimum expected output behavior:

- passing dataset:
  - `validation_status = passed`
  - all invalid counters are `0`
- failing dataset:
  - `validation_status = failed`
  - one or more invalid counters are greater than `0`
