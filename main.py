from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from typing import List

app = FastAPI()


@app.get("/ping")
def ping():
    return "pong"


class CarsModel(BaseModel):
    id: str
    brand: str
    model: str
    characteristics: object
    characteristics = {
        max_speed: int,
        max_fuel_capacity: int
    }


cars_store: List[CarsModel] = []


@app.post("/cars", status_code=201)
def create_cars(students: List[CarsModel]):
    cars_store.extend(students)
    return JSONResponse(cars_store, status_code=201)


@app.get("/cars")
def get_cars():
    return cars_store


@app.get("/cars-id")
def get_cars_id(id: str):
    if not id :
        return JSONResponse(cars_store, status_code=401)
    if id:
        return cars_store
