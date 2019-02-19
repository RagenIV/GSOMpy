# coding: utf-8

def upperator(s, n):
    if len(s) > n:
        return s.upper()
    else:
        return s

print(upperator("Строка для Примера", 5))
print(upperator("Строка для Примера", 42))
