from pydantic import BaseModel
from typing import ClassVar, List
from sqlalchemy import Boolean, ForeignKey, create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from database import Base

class Car(BaseModel):
    car_list = []
    year: int
    make: str
    model: str
    car_list: ClassVar[List['Car']] = [] ## On instantiation, adds new Car to class level list (like my capstone phrase generator)

    class Config:
        orm_mode = True

class CarDB(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    owner_id= Column(Integer, ForeignKey("Owner.id"))
    year = Column(Integer)
    make = Column(String)
    model = Column(String)
    owner = relationship("OwnerDB", back_populates="cars")

    def __repr__(self):
        return(f"Car | ID: {self.id} | Year: {self.year} | Make: {self.make} | Model: {self.model}")


class Owner(BaseModel):
    name: str
    regular_customer: bool

    class Config:orm_mode = True

class OwnerDB(Base):
    __tablename__ = "owners"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    regular_customer = Column(Boolean)
    cars = relationship("CarDB", back_populates="owner")

    def __repr__(self):
        return("Owner | ID: {self.id} | Name: {self.model} | Regular Customer ? {self.regular_customer}")
    

