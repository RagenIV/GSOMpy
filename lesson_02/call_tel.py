d = {343:15, 381:18, 473:13, 485:11}

cod = int(input("Ввдеите код города:\n"))
tim = float(input("Введите время переговоров в минутах:\n"))

if cod in d:
    print(round(d[cod]*tim, 2) ,"руб.")
else:
    print("Нет данных ")
