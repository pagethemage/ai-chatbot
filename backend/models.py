from pydantic import BaseModel

class CarCreate(BaseModel):
    year: int
    make: str
    model: str

