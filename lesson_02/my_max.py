# coding: utf-8

# вообще-то есть встроенная функция max()
def mymax(a, b):
    if a > b:
        return a
    else:
        return b

try:
    a, b = map(int, input("Введите два числа, разделённых пробелом\n").split())
    print("Наибольшее из двух чисел:", mymax(a,b))
except:
    print("Некорректный ввод")

