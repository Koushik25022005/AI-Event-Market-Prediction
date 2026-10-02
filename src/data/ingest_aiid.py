import pandas as pd
from pathlib import Path

RAW = Path("data/raw/aiid/")

def find_file(name: str) -> Path:
    matches = list(RAW.rglob(name))
    if not matches:
        raise FileNotFoundError(f"Could not find {name} under {RAW.resolve()}")
    return matches[0]


def load_incidents() -> pd.DataFrame:
    path = find_file("incidents.csv")
    print(f"Loading {path}")
    df = pd.read_csv(path)
    print(f"Columns: {df.columns.tolist()}")
    return df

if __name__ == "__main__":
    df = load_incidents()
    print(df.head())
