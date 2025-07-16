from fastapi import FastAPI
from models import Structure

app = FastAPI()




@app.post("/input")
def input(inp: Structure):
    return {"response"}
    