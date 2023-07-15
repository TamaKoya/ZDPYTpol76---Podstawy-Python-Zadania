lst =[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
index = 0

while index < len(lst):
    if lst[index] == 100:
        my_message =f"There is a 100 at index no: {index}"
        index += 1
    else:
        index += 1

print (my_message)