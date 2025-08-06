import csv
from datetime import datetime
import os

os.makedirs("corpus", exist_ok=True)

def log_to_corpus(text, privacy):
    with open("corpus/corpus_entries.csv", "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().isoformat(), text, privacy])
