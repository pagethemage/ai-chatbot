from fastapi import APIRouter
from .models import CarCreate
from .cars import Car

router = APIRouter()

@router.post("/cars")
def create_car(car_data: CarCreate):
    new_car = Car(car_data.year, car_data.model, car_data.make)
    return{"message": "Car created successfully", "car": new_car.to_dict()}

