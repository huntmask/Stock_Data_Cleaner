import pandas as pd


def clean_stock_data(df):
    print(df.isnull().sum())

    # Clean column names
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.capitalize()

    print("Original Columns:")
    print(df.columns)

    # Rename possible date columns
    if 'Timestamp' in df.columns:
        df.rename(columns={'Timestamp': 'Date'}, inplace=True)

    if 'Datetime' in df.columns:
        df.rename(columns={'Datetime': 'Date'}, inplace=True)

    if 'date' in df.columns:
        df.rename(columns={'date': 'Date'}, inplace=True)

    print("Updated Columns:")
    print(df.columns)

    # Check required columns
    required_columns = [
        'Date',
        'Open',
        'High',
        'Low',
        'Close',
        'Volume'
    ]

    for column in required_columns:

        if column not in df.columns:

            raise ValueError(
                f"Missing required column: {column}"
            )

    # Reset index
    df = df.reset_index(drop=True)

    # Convert date column
    df['Date'] = pd.to_datetime(df['Date'])

    # Fill missing values
    df = df.ffill()

    # Remove duplicates
    df = df.drop_duplicates()
    print(df.isnull().sum())


    return df