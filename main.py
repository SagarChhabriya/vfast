from fastapi import FastAPI
from pathlib import Path
import json

app = FastAPI()

@app.get("/")
async def hello_world():
    return {"message": "Hello World!"}

@app.get("/hello/{name}")
async def hello_name(name: str):
    return {"message": f"Hello {name}! 👋"}

@app.get("/health")
async def health_check():
    return {"status": "OK", "message": "API is running!"}


def load_data():
    with open("patients.json", "rb") as file:
        data = json.load(file)
    return data

@app.get("/view")
async def view_records():
    return load_data()