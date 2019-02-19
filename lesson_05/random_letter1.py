# coding: utf-8

import random

L = ['самовар', 'весна', 'лето']

word = random.choice(L)
n = random.randint(0,len(word)-1)

print(word[:n] + "?" + word[n+1:])
if word[n] == input("Введите букву: "):
    print("Победа!")
else:
    print("Увы! Попробуйте в другой раз.")

print("Слово:", word)
