class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def __init__(self, name, mileage, capacity):
        super().__init__(name, mileage, capacity)

    def fare(self):
        total_fare = super().fare()
        percentage = total_fare * 0.1
        return total_fare + percentage

School_Bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_Bus.fare())