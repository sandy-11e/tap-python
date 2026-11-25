import json

import pandas as pd


def load_column_mapping(config_path: str) -> dict[str, str]:
    """Load column mapping from a JSON configuration file."""

    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)

    return config["column_mapping"]


def standardize_columns(df, config_path):
    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)

    mapping = config["column_mapping"]

    return df.rename(columns=mapping)


def transform_dataframe(df):
    df = df.drop_duplicates()
    df.columns = df.columns.str.lower().str.strip()

    return df


def to_snake_case(columns):
    return [col.strip().lower().replace(" ", "_") for col in columns]


def convert_data_types(df):
    float_columns = ["price", "freight_value"]

    for col in float_columns:
        if col in df.columns:
            df[col] = df[col].astype(float)

    timestamp_columns = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ]

    for col in timestamp_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    return df


def calculate_order_totals(data):
    order_totals = {}

    for row in data:
        order_id = row["order_id"]
        total = float(row["price"]) + float(row["freight_value"])

        if order_id in order_totals:
            order_totals[order_id] += total
        else:
            order_totals[order_id] = total

    return order_totals
