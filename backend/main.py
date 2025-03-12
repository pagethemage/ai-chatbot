from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware 
from pydantic import BaseModel 
from typing import List
from fastapi import APIRouter
from api import router
from models import Car


app = FastAPI()
app.include_router(router)



## TODO:

## Maybe focus on integrating AI first, getting the API calls and conversation working
    ## then implement SQL database 

## Install cookiecutter to ensure my app follows FastAPI conventions
## Understand SQLalchemy and its ORM further
## Implement more class
## Expriment with SQL queries
