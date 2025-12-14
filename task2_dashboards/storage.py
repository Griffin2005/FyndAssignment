import csv
import os
from datetime import datetime

DATA_PATH = "data/reviews.csv"

def init_storage():
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(DATA_PATH):
        with open(DATA_PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "timestamp",
                "rating",
                "review",
                "ai_response",
                "ai_summary",
                "recommended_action"
            ])

def save_review(rating, review, ai_response, ai_summary, action):
    with open(DATA_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().isoformat(),
            rating,
            review,
            ai_response,
            ai_summary,
            action
        ])

def read_reviews():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))
