from fastapi import FastAPI
from pydantic import BaseModel
import boto3

app = FastAPI()
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('GolfWatchUsers')

class Preference(BaseModel):
    phone: str
    email: str
    course_id: str
    start_time: str  # e.g., "07:00"
    end_time: str    # e.g., "09:30"

@app.post("/register")
def register(preference: Preference):
    table.put_item(Item=preference.dict())
    return {"status": "registered"}
