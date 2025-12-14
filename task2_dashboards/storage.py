import csv
import os
from datetime import datetime
import subprocess

DATA_PATH = "task2_dashboards/data/reviews.csv"

def init_storage():
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)

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
    init_storage()

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

    # Push update to GitHub
    subprocess.run(["git", "add", DATA_PATH])
    subprocess.run(["git", "commit", "-m", "Update reviews data"])
    subprocess.run(["git", "push"])

def read_reviews():
    init_storage()

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))
