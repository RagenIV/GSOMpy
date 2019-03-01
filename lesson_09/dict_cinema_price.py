# coding: utf-8

res = 0

movies = {"Пятница":{12:250, 16:350, 20:450},"Чемпионы":{10:250, 13:350, 16:350},"Пернатая банда":{10:350, 14:450, 18:450}}

try:
    print("Программа для подсчета стоимости билетов в кино.")
    mov = input("Выбрать фильм: ")
    day = input("Выбрать день (сегодня, завтра): ")
    tim = int(input("Выбрать время: "))
    k = int(input("Выбрать количество билетов: "))
    print("Выбрали фильм:", mov, "День:", day, "Время:", tim, "Количество билетов:", k)
    res = movies[mov][tim]
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
