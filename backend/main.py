from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware 
from pydantic import BaseModel 
from typing import List
from fastapi import APIRouter
from .api import router


# class Fruit(BaseModel):
#     name: str 


# class Fruits(BaseModel):
#     fruits: List[Fruit]

# app = FastAPI()
# origins = [
#     "http://localhost:3000",
# ]

# app.add_middleware(
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app = FastAPI()


class Item(BaseModel): 
    text:str
    is_done:bool = False

items:list = []

class Car():
    def __init__(self, year, model, make):
        self._year = year
        self._model = model
        self._make = make
        car_list = []
        car_list.append(Car)

    @property
    def year(self):
        return self._year

    @property 
    def model(self):
        return self._model
    
    @property
    def make(self):
        return self._make


    

# @app.post("/cars")
# def create_car(new_car(self, year, model, make):Car):
#     Car new_car


@router.get("/")
def root():
    return{"Hello": "World"}




@router.post("/items")
def create_item(item:Item):
    items.append(item)
    return items

@router.get("/items")
def list_items(limit: int = 10):
    return items[0:limit]

@router.get("/items/{item_id}")
def get_item(item_id:int) -> Item:
    if item_id < len(items):
        item = items[item_id]
        return item
    else:

        raise(HTTPException(status_code=404, detail=f"404: Index {item_id} was not found in list. "))
