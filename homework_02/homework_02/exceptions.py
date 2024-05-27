class Error(Exception):
     def cargoerror(self):
          print("CarGoOverlord")
     
     def lowfuelerror(self):
          print("LowFuelError")
     
     def fuelerror(self):
          print("NotEnoughFuelError")


    
exception = Error()

def main():
     exception.cargoerror()
     exception.fuelerror()
     exception.lowfuelerro()


if __name__=="main":
     main()
        
