from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel 

app = FastAPI()

class Item(BaseModel): 
    text:str
    is_done:bool = False

items:list = []

@app.get("/")
def root():
    return{"Hello": "World"}


@app.post("/items")
def create_item(item:Item):
    items.append(item)
    return items

@app.get("/items")
def list_items(limit: int = 10):
    return items[0:limit]

@app.get("/items/{item_id}")
def get_item(item_id:int) -> Item:
    if item_id < len(items):
        item = items[item_id]
        return item
    else:

        raise(HTTPException(status_code=404, detail=f"404: Index {item_id} was not found in list. "))
