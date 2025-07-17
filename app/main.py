from fastapi import FastAPI
from models import Structure

app = FastAPI()

@app.post("/generate")
def generate(inp: Structure):
    return {"response"}
    