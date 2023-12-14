
# parent class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def print_info(self):
        print(f"Make: {self.make}\nModel: {self.model}")
#child class
class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def print_info(self):
        super().print_info()
        print(f"Year: {self.year}")
#child class
class Truck(Vehicle):
    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.capacity = capacity

    def print_info(self):
        super().print_info()
        print(f"Capacity: {self.capacity} tons")

car = Car("Toyota", "Camry", 2022)
truck = Truck("Ford", "F-150", 3)

car.print_info()
print()
truck.print_info()
