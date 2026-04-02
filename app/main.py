from fastapi import FastAPI
from .calculator import sum, resta, multiply

app = FastAPI()

@app.post("/sum")
def endpoint_sum(a: int, b: int):
    return {"result": sum(a, b)}

@app.post("/resta")
def endpoint_resta(a: int, b: int):
    return {"result": resta(a, b)}

@app.post("/multiply")
def endpoint_multiply(a: int, b: int):
    return {"result": multiply(a, b)}