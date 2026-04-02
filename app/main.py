from fastapi import FastAPI
from pydantic import BaseModel
from . import calculator

app = FastAPI()


class Operands(BaseModel):
    a: int
    b: int


@app.post("/suma")
def endpoint_suma(operands: Operands):
    return {"resultado": calculator.sum(operands.a, operands.b)}


@app.post("/resta")
def endpoint_resta(operands: Operands):
    return {"resultado": calculator.resta(operands.a, operands.b)}


@app.post("/multiplicacion")
def endpoint_multiplicacion(operands: Operands):
    return {"resultado": calculator.multiply(operands.a, operands.b)}