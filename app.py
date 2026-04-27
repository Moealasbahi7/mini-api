from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from mini-api"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/hello")
def hello():
    return {"message": "hello"}

@app.get("/mia")
def mia():
    return {"message": "added by mia"}