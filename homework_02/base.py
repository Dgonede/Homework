from abc import ABC
from exceptions import NotEnoughFuelError, LowFuelError



class Vehicle(ABC):
    
    def __init__(self, weight, started, fuel, fuel_consumption, cargo, max_cargo):
        self.weight = weight
        self.weight = 500
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = 1
        self.fuel = 40
        self.fuel_consumption = 12
        self.max_cargo = max_cargo
        self.max_cargo = 700
        self.cargo = cargo
        self.cargo = 100
        self.distance = 0

    def read_vehicle(self):
        """Метод выводит данные по Vehicle"""
        long_name = print(f"Weight = {self.weight} Kg, Started = {self.started}, Fuel = {self.fuel}-L, Fuel_comsumption = {self.fuel_consumption}-L, Cargo {self.cargo}Kg, Max_cargo {self.max_cargo} Kg")
        return long_name    

    def start(self):
        """Метод проверяет значение start и fuel"""
        if self.started > 0 and self.fuel > 0:
                print(f"started {self.started}")
        
        elif self.started == 0 and self.fuel > 0:
             print(f"can start, fuel is {self.fuel}L")
        else:        
            raise LowFuelError("Ошибка: Малый запас топлива")
    


              
        
        
    def move(self):
        """Метод производит пробег исходя из топлива в баке"""
        if self.fuel > 0 and self.started > 0:
                self.distance = int(self.fuel / self.fuel_consumption * 100)
                print(f"distance = {self.distance} km")
        elif self.started == 0:
                print("Chek fuel")
               
        else:
            raise NotEnoughFuelError("Ошибка: Недостаточно топлива")
        
        

            
            
           
           
            
my_car_go = Vehicle("weight", "started", "fuel", "fuel_consumption","cargo", "max_cargo")


def main():
    my_car_go.read_vehicle()
    print()
    my_car_go.move()
    print()
    my_car_go.start()
    
    
     
                          
            


if __name__=="__main__":
    main()


               

                                   

    

    

             