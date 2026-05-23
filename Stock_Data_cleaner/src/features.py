import pandas as pd


def add_features(df):

    # Moving averages
    df['MA_5'] = df['Close'].rolling(window=5).mean()

    df['MA_10'] = df['Close'].rolling(window=10).mean()

    # Daily returns
    df['Daily_Return'] = df['Close'].pct_change()

    # Volatility
    df['Volatility'] = (
        df['Daily_Return']
        .rolling(window=10)
        .std()
    )

    # RSI
    delta = df['Close'].diff()

    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss

    df['RSI'] = 100 - (100 / (1 + rs))

    # Bollinger Bands
    df['Middle_Band'] = (
        df['Close']
        .rolling(window=20)
        .mean()
    )

    std_dev = (
        df['Close']
        .rolling(window=20)
        .std()
    )

    df['Upper_Band'] = (
        df['Middle_Band'] + (2 * std_dev)
    )

    df['Lower_Band'] = (
        df['Middle_Band'] - (2 * std_dev)
    )

    # Remove nulls
    df = df.dropna()

    return df