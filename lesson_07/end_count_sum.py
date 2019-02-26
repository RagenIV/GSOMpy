# coding: utf-8
s = 0
ss = ""
ss = input("Введите число или Стоп для выхода: ").lower()
while ss != "стоп":
    try:
        s += int(ss)
    except:
        print("Ошибка ввода.")
    ss = input("Введите число или Стоп для выхода: ").lower()
print("Сумма: "+str(s))
