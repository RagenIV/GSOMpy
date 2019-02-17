# coding: utf-8

def even(x):
    return x%2==0

value = input("Введите целое число\n")
if value:
    try:
        num = int(value)
        if even(num):
            print("Чётное")
        else:
            print("Нечётное")
    except:
        print("Некорректный ввод")
else:
    print("Пустой ввод")
