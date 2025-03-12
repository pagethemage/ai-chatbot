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
