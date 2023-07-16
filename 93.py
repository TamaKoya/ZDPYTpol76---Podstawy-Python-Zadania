class Vehicle:
    def __init__(self, max_speed: int = 100, mileage: int = 0):
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity: int):
        return f"seating capacity is {capacity}"

class Bus(Vehicle):
    def seating_capacity(self, capacity: int = 50):
        return super().seating_capacity(capacity)

bus_obj = Bus(100000)
print(bus_obj.seating_capacity())