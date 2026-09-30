import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")

project_name = "ai-event-prediction"

list_of_files = [
    ".github/workflows/python-ci.yml",
    ".github/workflows/lin-test.yml",
    ".github/ISSUE_TEMPLATE",
    "data/raw",
    "data/processed",
    "data/interim",
    "data/external",
    "notebooks/01_data_ingestion.ipynb",
    "notebooks/02_eda.ipynb",
    "notebooks/03_feature_engineering.ipynb",
    "notebooks/04_model_training.ipynb",
    "notebooks/05_backtesting.ipynb",
    "src/data/ingest_market.py",
    "src/data/ingest_news.py",
    "src/data/build_event_timeline.py",
    "src/features/build_features.py",
    "src/sentiment/analyze_sentiment.py",
    "src/models/train_model.py",
    "src/models/evaluate_model.py",
    "src/models/predict_model.py",
    "utils/config.py",
    "utils/logger.py",
    "tests/test_ingestion.py",
    "tests/test_features.py",
    "tests/test_model.py",
    "docs/architectre.md",
    "docs/data_dictionary.md",
    "docs/methodology.md",
    "Makefile",
    ".gitattributes",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")