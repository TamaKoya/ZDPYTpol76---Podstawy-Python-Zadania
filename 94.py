class Vehicle:
    color = "White"
    def __init__(self, max_speed: int=100, mileage: int=0):
        self.max_speed = max_speed
        self.mileage = mileage

veh_obj = Vehicle()
print(veh_obj.color)