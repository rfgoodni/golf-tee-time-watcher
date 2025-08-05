import requests
from datetime import datetime
import os

def fetch_tee_times(course_id, date, start_time, end_time):
    url = "https://partners.golfnow.com/api/v2/tee-times"
    headers = {"Authorization": f"Bearer {os.getenv('GOLFNOW_API_KEY')}"}
    params = {
        "course_id": course_id,
        "date": date,
        "start_time": start_time,
        "end_time": end_time,
        "holes": 18,
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json().get("tee_times", [])
