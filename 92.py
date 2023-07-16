class Vehicle:
    def __init__(self, max_speed: int, mileage: int):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, mileage):
        super().__init__(90, mileage)