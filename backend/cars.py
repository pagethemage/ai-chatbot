class Car:
    car_list = []

    def __init__(self, year:int, make:str, model:str):
        self.year = year
        self.make = make
        self.model = model
        Car.car_list.append(self) ## On instantiation, adds new Car to class level list (like my capstone phrase generator)

    def to_dict(self):
        return{"year":self.year, "model":self.model, "make":self.make}
    
