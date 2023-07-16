class Vehicle:
    def __init__(self, name, milelage, capacity):
        self.name = name
        self.mileage = milelage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

print(type(School_bus))
print(isinstance(School_bus, Vehicle))