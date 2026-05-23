import yfinance as yf


def download_stock_data(ticker, start, end):

    df = yf.download(
        ticker,
        start=start,
        end=end,
        auto_adjust=True
    )

    # Handle missing data and flatten multi-index columns if present
    if df is None:
        return df

    if df.columns.nlevels > 1:
        df.columns = df.columns.get_level_values(0)

    return df