L = [2, 4, 9, 16, 25]

# 1
L1 = []
for i in L:
    L1.append(i ** 0.5)
print(L1)

# 2
L2 = list(map(lambda x: x ** 0.5, L))
print(L2)

# 3
L3 = [i ** 0.5 for i in L]
print(L3)
