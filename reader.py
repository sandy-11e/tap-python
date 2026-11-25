
import csv
import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class DataReadError(Exception):
    """Raised when a CSV file cannot be read."""


class ConfigError(Exception):
    """Raised when configuration cannot be loaded."""


def read_csv(path, column_mapping=None):
    try:
        logger.info("Reading CSV: %s", path)

        with open(path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            records = []

            for row in reader:
                if column_mapping:
                    row = {
                        column_mapping.get(column, column): value
                        for column, value in row.items()
                    }

                records.append(row)

            logger.info("Successfully read %s records from %s", len(records), path)
            return records

    except (OSError, csv.Error) as e:
        logger.exception("Failed to read CSV: %s", path)
        raise DataReadError(f"Failed to read {path}: {e}") from e


def read_all_csv(directory, config_path="config.json"):
    try:
        with open(config_path, "r", encoding="utf-8") as file:
            config = json.load(file)

        logger.info("Configuration loaded successfully")

    except (OSError, json.JSONDecodeError) as e:
        logger.exception("Failed to load configuration")
        raise ConfigError(f"Failed to load configuration: {e}") from e

    column_mapping = config.get("column_mapping", {})
    directory = Path(directory)
    datasets = {}

    for file_path in directory.glob("*.csv"):
        logger.info("Processing dataset: %s", file_path.name)

        datasets[file_path.stem] = read_csv(
            file_path, column_mapping
        )

    logger.info("Successfully processed %s CSV files", len(datasets))

    return datasets
