dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

lst = [name.upper() for name, value in dict1.items() if value < 5000]

print(lst)