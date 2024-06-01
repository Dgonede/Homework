from abc import ABC
from exceptions import LowFuelError, NotEnoughFuel



class Vehicle(ABC):
    def __init__(self, weight, started, fuel, fuel_consumption, cargo, max_cargo):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.max_cargo = max_cargo
        self.cargo = cargo
        self.distance = 0

    
    def read_vehicle(self, weight, started, fuel, fuel_consumption, cargo, max_cargo):
        """Метод выводит данные по Vehicle"""
        long_name = print(f"Weight = {weight} Kg, Started = {started}, Fuel = {fuel}-L, Fuel_comsumption = {fuel_consumption}-L, Cargo {cargo}Kg, Max_cargo {max_cargo} Kg")
        return long_name    

    
    def start(self, fuel, started):
        """Метод проверяет значение start и fuel"""
        if started > 0 and fuel > 0:
                print(f"started {started}")
        
        elif started == 0 and fuel > 0:
             print(f"can start, fuel is {fuel}L")
        else:        
            raise LowFuelError("Ошибка: Малый запас топлива")
    


              
        
        
    def move(self, fuel, started, fuel_consumption):
        """Метод производит пробег исходя из топлива в баке"""
        if fuel > 0 and started > 0:
                self.distance = int(fuel / fuel_consumption * 100)
                print(f"distance = {self.distance} km")
        elif started == 0:
                print("Chek fuel")
               
        else:
            raise NotEnoughFuel("Ошибка: Недостаточно топлива")
        
        

            
            
           
           
            
my_car_go = Vehicle("weight", "started", "fuel", "fuel_consumption","cargo", "max_cargo")


def main():
    my_car_go.read_vehicle(300, 1, 40, 12, 400, 700)
    print()
    my_car_go.move(0,1,0)
    print()
    my_car_go.start(0,0)
    
    
     
                          
            


if __name__=="__main__":
    main()


               

                                   

    

    

             