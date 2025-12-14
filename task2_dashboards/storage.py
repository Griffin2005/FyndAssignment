import requests
from datetime import datetime

# PASTE YOUR APPS SCRIPT WEB APP URL HERE
APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzMWeetkU5BIn7YA5GSRznBMSRizlg9NOhTHIEIj206A0KKI79hzHLoI0hPO1Ra2QHPbw/exec"


def save_review(rating, review, ai_response, ai_summary, action):
    payload = {
        "timestamp": datetime.now().isoformat(),
        "rating": rating,
        "review": review,
        "ai_response": ai_response,
        "ai_summary": ai_summary,
        "recommended_action": action
    }

    response = requests.post(APPS_SCRIPT_URL, json=payload, timeout=30)
    response.raise_for_status()


def read_reviews():
    response = requests.get(APPS_SCRIPT_URL, timeout=30)
    response.raise_for_status()
    return response.json()
