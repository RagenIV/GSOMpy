# coding: utf-8
# pprint выводит не так красиво, как в логах

tasks = []
while True:
    print("""Простой todo: 
        1. Добавить задачу.
        2. Вывести список задач.
        3. Выход.
    """)
    try:
        n = int(input("Укажите число: "))
        if n == 1:
            t = {}
            t["name"] = input("Сформулируйте задачу: ")
            t["category"] = input("Добавьте категорию к задаче: ")
            t["time"] = input("Добавьте время к задаче: ")
            tasks.append(t)
        elif n == 2:
            for i in tasks:
                print("Задача: {p[name]}\nКатегория: {p[category]}\nДата: {p[time]}".format(p=i))
        elif n == 3:
            break
        else:
            print("Выберете доступный пункт меню.")
    except:
        print("Выберете доступный пункт меню.")
