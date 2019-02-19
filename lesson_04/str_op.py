# coding: utf-8

s = "У лукоморья 123 дуб зеленый 456"
# буква != символ
sL = s.lower()

# 1
p = sL.find("я")
if p == -1:
    print("В строке нет буквы 'я'")
else:
    print("Индекс буквы 'я' в строке: {n}".format(n=p))

# 2
print("Буква 'у' в строке встречается {n} раз".format(n=sL.count("у")))

# 3
if not(s.isupper()):
    print(s.upper())

# 4
if len(s) > 4:
    print(sL)

# 5
print('О'+s[1:])
