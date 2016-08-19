import random
rnd = random.randint(0, 100)
i = 0
while True:
    i += 1
    num = int(input("Введите число в диапазоне [0, 100]: "))
    if num == rnd:
        print("Ты молодец! Угадал число с", i, " попытки")
        break
    elif num > rnd:
        print("Зададанное число меньше")
    else:
        print("Зададанное число больше")
    if i == 10:
        print("Ты не угадал загаданное число", rnd)
        break
print ("Конец игры")

