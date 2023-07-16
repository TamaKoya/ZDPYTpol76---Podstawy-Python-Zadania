f = open("plik4.txt", "a")
f.write("Hello there\n")
f.close()

with open("plik4.txt") as f:
    line = f.readline()
    print(line)