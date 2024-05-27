from homework_02.base import Vehicle
from homework_02.engine import Engine as en

class Car(Vehicle, en):
   
   def set_engine(self):
        return en.engine()
my_car = en()
  


def car_engine():
    my_car.engine(3,5)


if __name__=="__main__":
    car_engine()