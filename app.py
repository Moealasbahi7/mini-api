from fastapi import FastAPI
from datetime import datetime
from google.cloud import storage
import json
import vertexai
from vertexai.generative_models import GenerativeModel

app = FastAPI()

vertexai.init(project="mini-api-493010", location="us-central1")

BUCKET_NAME = "mini-api-bucket-123"
FILE_NAME = "data.json"


@app.get("/")
def root():
    return {"message": "Mini API working "}

@app.get("/hello")
def hello():
    return {"message": "hello"}

@app.get("/status")
def status():
    return {"time": str(datetime.now())}


def get_bucket():
    client = storage.Client()
    return client.bucket(BUCKET_NAME)

@app.get("/data")
def get_data():
    bucket = get_bucket()
    blob = bucket.blob(FILE_NAME)

    if not blob.exists():
        return []

    data = blob.download_as_text()
    return json.loads(data)

@app.post("/data")
def post_data(item: dict):
    bucket = get_bucket()
    blob = bucket.blob(FILE_NAME)

    try:
        data = json.loads(blob.download_as_text())
    except:
        data = []

    data.append(item)

    blob.upload_from_string(json.dumps(data))

    return {"message": "added", "data": item}


@app.get("/poem")
def poem():
    try:
        model = GenerativeModel("gemini-1.5-flash")
        response = model.generate_content("Write a short poem about life")
        return {"poem": response.text}
    except Exception as e:
        return {"error": str(e)}