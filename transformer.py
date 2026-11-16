def transform_dataframe(df):
    df = df.drop_duplicates()
    df.columns = df.columns.str.lower().str.strip()

    return df