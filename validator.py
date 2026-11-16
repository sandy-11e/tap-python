def validate_dataframe(df):
    print("Shape:", df.shape)
    print("Null values:", df.isnull().sum().sum())
    print("Duplicate rows:", df.duplicated().sum())

    return df