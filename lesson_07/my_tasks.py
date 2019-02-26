# coding: utf-8
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
            t = []
            t.append(input("Сформулируйте задачу: "))
            t.append(input("Добавьте категорию к задаче: "))
            t.append(input("Добавьте время к задаче: "))
            tasks.append(t)
        elif n == 2:
            for i in tasks:
                print("Задача: {p[0]} Категория: {p[1]} Дата: {p[2]}".format(p=i))
        elif n == 3:
            break
        else:
            print("Выберете доступный пункт меню.")
    except:
        print("Выберете доступный пункт меню.")
