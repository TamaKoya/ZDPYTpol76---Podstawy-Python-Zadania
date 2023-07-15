lst1 = [3.14, 66, "Teddy Bear", True, [], {}]
lst2 = []

for element in lst1:
    lst2.append(type(element))

print(lst2)