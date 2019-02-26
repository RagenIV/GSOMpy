# coding: utf-8

s = '''В разные эпохи и у разных народов число Пи имело разное значение.
Например, в Древнем Египте оно равнялось 3.1604 у индусов оно приобрело
значение 3.162 китайцы пользовались числом, равным 3.1459
Буквенное обозначение число Пи получило только в 1706 году – оно происходит
от начальных букв двух греческих слов, означающих окружность и периметр.
Буквой π число наделил математик Джонс, а прочно вошла в математику она
уже в 1737 году.'''

numL = list(filter(lambda x: x.find(".")==x.rfind(".") and x.replace(".","").isdigit(), s.split()))
num = list(map(lambda x: float(x), numL))

print("Числа в тексте: "+(" ".join(numL)))
print("Всего "+str(len(numL))+" чисел в тексте")
print("Сумма: "+str(sum(num)))
print("Максимальное число: "+str(max(num)))