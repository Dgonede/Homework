from homework_02.exceptions import CarGoOverlordError
from homework_02.base import Vehicle


class Plane(Vehicle):
     def __init__(self, cargo, weight, started, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, started, fuel, fuel_consumption, cargo, max_cargo)
        
        
        

     def load_cargo(self):
        """Метод проверяет перегруз"""
        
        if self.cargo + self.weight <= self.max_cargo:
                print(f"Now cargo = {self.cargo + self.weight} Kg")
                
        else:
            raise CarGoOverlordError(f"Ошибка: Перегруз на {self.cargo + self.weight - self.max_cargo} kg")
       
        
        

        

     def remove_all_cargo(self):
         """Метод сбрасывает вес"""
         a = self.cargo
         if a > 0:
             a = 0
             print(f"cargo is remove {a}, it was {self.cargo} Kg befor remove")
         
         
             
         
my_car = Plane("cargo", "weight", "started", "fuel", "fuel_consumption", "max_cargo")

def main():
    my_car.read_vehicle()
    my_car.load_cargo()
    my_car.remove_all_cargo()
    
    
     
                          
            


if __name__=="__main__":
    main()