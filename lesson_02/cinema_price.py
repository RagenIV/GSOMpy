# coding: utf-8

res = 0

try:
    print("Программа для подсчета стоимости билетов в кино.")
    mov = input("Выбрать фильм: ")
    day = input("Выбрать день (сегодня, завтра): ")
    tim = int(input("Выбрать время: "))
    k = int(input("Выбрать количество билетов: "))
    print("Выбрали фильм:", mov, "День:", day, "Время:", tim, "Количество билетов:", k)
    if mov == "Пятница":
        if tim == 12:
            res = 250
        elif tim == 16:
            res = 350
        elif tim == 20:
            res = 450
        else:
            print("Нет сеанса в это время")
    elif mov == "Чемпионы":
        if tim == 10:
            res = 250
        elif tim == 13:
            res = 350
        elif tim == 16:
            res = 350
        else:
            print("Нет сеанса в это время")
    elif mov == "Пернатая банда":
        if tim == 10:
            res = 350
        elif tim == 14:
            res = 450
        elif tim == 18:
            res = 450
        else:
            print("Нет сеанса в это время")
    else:
        print("Нет такого фильма")
    if k >= 20:
        res *= 0.8
    if day == "завтра":
        res *= 0.95
    elif day != "сегодня":
        print("Билеты только на сегодня и завтра!")
    if res > 0:
        print("Результат", round(res*k, 2))
except:
    print("Ошибка ввода.")

