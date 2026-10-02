import yfinance as yf
import pandas as pd
from pathlib import Path

def load_markets(tickers: list[str], start="2015-01-01", out="data/raw/market/prices.parquet") -> pd.DataFrame:
    px = yf.download(tickers, auto_adjust=True, start=start, progress=False)["Close"]
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    px.to_parquet(out)
    return px

if __name__ == "__main__":
    load_markets(["^GSPC", "^IXIC","AAPL", "MSFT", "GOOG", "AMZN", "TSLA"])