# coding: utf-8

import random

attempts = 3
m = 2**attempts
x = random.randint(1, m)

print("Компьютер загадал натуральное число, не превосходящее "+str(m))
print("У Вас есть "+str(attempts)+" попытки. Удачи!")

while attempts > 0:
    attempts -= 1
    s = input("Попробуйте угадать: ")
    if s == "Выход":
        print("Вы добровольно покинули игру.")
        attempts = -2
        break
    try:
        t = int(s)
        if t == x:
            attempts = -1
            print("Победа!")
        elif t > x:
            print("Попробуйте число меньше!")
        else:
            print("Попробуйте число больше!")
    except:
        print("Введите число!")
        attempts += 1

if attempts == 0:
    print("Game over!")
    print("Число: "+str(x))
