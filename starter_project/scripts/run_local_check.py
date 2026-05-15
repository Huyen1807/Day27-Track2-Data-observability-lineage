from __future__ import annotations

import argparse
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from src.validation import LabValidationError, run_lab_check


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the lab validation logic without Airflow.")
    parser.add_argument("input_file", help="CSV file to validate.")
    parser.add_argument("--output", default=str(PROJECT_ROOT / "output" / "validation_summary.json"))
    parser.add_argument("--allow-failure", action="store_true")
    parser.add_argument("--skip-discord", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_file = Path(args.input_file).expanduser()
    if not input_file.is_absolute():
        input_file = (Path.cwd() / input_file).resolve()

    output_file = Path(args.output).expanduser()
    if not output_file.is_absolute():
        output_file = (Path.cwd() / output_file).resolve()

    try:
        summary = run_lab_check(
            input_path=input_file,
            output_path=output_file,
            allow_failure=args.allow_failure,
            skip_discord=args.skip_discord,
        )
    except LabValidationError as exc:
        print(exc)
        return 1

    print(summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
