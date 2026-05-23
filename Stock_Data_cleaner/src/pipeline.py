import pandas as pd

from download import download_stock_data
from clean import clean_stock_data


# -----------------------------
# SETTINGS
# -----------------------------
USE_CSV = True

CSV_PATH = "../data/raw/AAPL_5min_sample.csv"

START_DATE = "2020-01-01"
END_DATE = "2025-01-01"


# -----------------------------
# LOAD DATA
# -----------------------------

if USE_CSV:
    TICKER = "Online"

    print("                     Loading CSV File...")

    df = pd.read_csv(CSV_PATH)

else:
    TICKER = "AAPL"

    print("                     Downloading Stock Data...")

    df = download_stock_data(
        ticker=TICKER,
        start=START_DATE,
        end=END_DATE
    )


# -----------------------------
# CLEAN DATA
# -----------------------------
print("                         Cleaning Data...")

df = clean_stock_data(df)

# -----------------------------
# SAVE CLEANED DATA
# -----------------------------

output_path = f"../data/cleaned/{TICKER}_cleaned.csv"

df.to_csv(output_path, index=False)

print("                            Pipeline Completed")
print(f"Saved at: {output_path}")