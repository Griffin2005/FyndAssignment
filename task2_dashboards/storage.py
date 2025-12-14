import requests
from datetime import datetime

APPS_SCRIPT_URL = "PASTE_YOUR_WEB_APP_URL_HERE"

def save_review(rating, review, ai_response, ai_summary, action):
    payload = {
        "timestamp": datetime.now().isoformat(),
        "rating": rating,
        "review": review,
        "ai_response": ai_response,
        "ai_summary": ai_summary,
        "recommended_action": action
    }

    requests.post(APPS_SCRIPT_URL, json=payload)


def read_reviews():
    response = requests.get(https://script.google.com/macros/s/AKfycbxVwrknbpAyilYPqp2Y2aIOkVr5BntTnnYF2I5feC-Q/dev)
    return response.json()
