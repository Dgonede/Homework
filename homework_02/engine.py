from dataclasses import dataclass

@dataclass
class Engine():
    def engine(self,volume, pistons):
        self.volume = volume
        self.pistons = pistons
        print(f"Volume - {self.volume}L, Pistons - {self.pistons}")
        

my_engine = Engine()

def main():
    my_engine.engine(3, "Autowelt Германия")   


if __name__=="__main__":
    main()