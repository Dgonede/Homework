from homework_02.exceptions import CargoOverload
from homework_02.base import Vehicle


class Plane(Vehicle):
     def load_cargo(self, cargo, weight, max_cargo):
        """Метод проверяет перегруз"""
        
        if cargo + weight <= max_cargo:
                print(f"Now cargo = {cargo + weight} Kg")
                
        else:
            raise CargoOverload(f"Ошибка: Перегруз на {cargo + weight - max_cargo} kg")
       
        
        

        

     def remove_all_cargo(self, cargo):
         """Метод сбрасывает вес"""
         a = cargo
         if a > 0:
             a = 0
             print(f"cargo is remove {a}, it was {cargo} Kg befor remove")
         
         
             
         


def main():
    my_plane = Plane("cargo", "weight", "started", "fuel", "fuel_consumption", "max_cargo")    
    my_plane.load_cargo(300,400,700)
    my_plane.remove_all_cargo(300)
    
    
     
                          
            


if __name__=="__main__":
    main()