# coding: utf-8

a, b = 1, 4

import random
steps = 0
x = random.randint(a, b)
y = b + 1
print("Компьютер загадал случайное целое число от", a, "до", b)
print("Попытайтесь угадать это число")
while x-y:
    steps += 1
    y = int(input())
    if not(x-y):
        print("Победа")
    elif x-y > 0:
        print("Больше")
    else:
        print("Меньше")
print("Вы справились за", steps, "попыток")
