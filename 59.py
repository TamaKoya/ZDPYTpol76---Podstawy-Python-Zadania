lst1 = ["Joe", "Sarah", "Mike", "Jess", "", "Matt", "Greg"]
index = 0
lst_new = []

while index < len(lst1):
    if lst1[index] != "":
        lst_new.insert(index, lst1[index])
        index += 1
    else:
        index += 1
print(lst_new)