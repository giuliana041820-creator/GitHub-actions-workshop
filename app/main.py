from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .calculator import sum, resta, multiply

app = FastAPI()

class OperationInput(BaseModel):
    a: int
    b: int

@app.post("/suma")
def suma_endpoint(data: OperationInput):
    return {"resultado": sum(data.a, data.b)}

@app.post("/resta")
def resta_endpoint(data: OperationInput):
    return {"resultado": resta(data.a, data.b)}

@app.post("/multiplicacion")
def multiplicacion_endpoint(data: OperationInput):
    return {"resultado": multiply(data.a, data.b)}
