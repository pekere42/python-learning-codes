class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        print(f"{self.model} car created")
    def created_car(self):
        print(f" {self.make} {self.model} {self.year} created")

my_car = Car("Audi","a3",2010)
my_car.created_car()