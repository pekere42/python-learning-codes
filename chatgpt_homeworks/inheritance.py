class Car():
    def __init__(self,make,model,year,age):
        self.make = make
        self.model = model
        self.year = year
        self.age = age
        print(f"{self.make} car created")
class electric_car(Car):
    def __init__(self,make,model,year,age,motortype):
        super().__init__(make,model,year,age)#pulling all features from parent class
        self.new_motortype = motortype#due to adding new features for child class
    def welcome(self):
        print(f"Welcome {self.make} {self.model} {self.year} to the factory")


tesla = electric_car("tesla","z3",2010,15,"electric")
tesla.welcome()