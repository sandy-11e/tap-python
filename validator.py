
import pandas as pd


def validate_dataframe(df):
    bad_records = df[df.isnull().any(axis=1)].copy()
    valid_records = df[df.notnull().all(axis=1)].copy()

    bad_records.to_csv("bad_records.csv", index=False)

    print("Total records:", len(df))
    print("Valid records:", len(valid_records))
    print("Bad records:", len(bad_records))

    return valid_records, bad_records
