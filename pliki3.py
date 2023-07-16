import random
i = 0
with open("liczby.txt", "w") as file:
    while i <= 100:
        line = random.randint(0, 2137)
        print(f"{line} : {line ** 2}\n", file=file)
        i += 1