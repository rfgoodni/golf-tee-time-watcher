import boto3
from golfnow import fetch_tee_times
from notify import send_sms
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('GolfWatchUsers')

def handler(event=None, context=None):
    users = table.scan().get("Items", [])
    today = datetime.now().strftime("%Y-%m-%d")

    for user in users:
        tee_times = fetch_tee_times(
            course_id=user["course_id"],
            date=today,
            start_time=user["start_time"],
            end_time=user["end_time"]
        )
        if tee_times:
            message = f"Tee time available at course {user['course_id']} between {user['start_time']} and {user['end_time']}"
            send_sms(user["phone"], message)
