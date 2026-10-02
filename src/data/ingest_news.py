from pathlib import Path
from datasets import load_dataset

DATASET_ID = "FinEredium1/Forecast-Dojo"
DIR = Path("data/raw/news")

def load_news_db():
    DIR.parent.mkdir(parents=True, exist_ok=True)
    dataset = load_dataset(DATASET_ID)
    print(dataset)
    dataset.save_to_disk(DIR)

if __name__ == "__main__":
    load_news_db()