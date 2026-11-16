COLUMN_MAPPING = {
    "customer_id": "customer_id",
    "customer_unique_id": "unique_customer_id",
    "customer_zip_code_prefix": "postal_code",
    "customer_city": "city",
    "customer_state": "state",

    "order_id": "order_id",
    "order_status": "status",
    "order_purchase_timestamp": "purchase_date",

    "product_id": "product_id",
    "product_category_name": "category"
}

def standardize_columns(df):
    df = df.rename(columns=COLUMN_MAPPING)
    return df

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
        "order_estimated_delivery_date"
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