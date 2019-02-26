def y(x):
    return x*x + 3

def masy(r):
    s = []
    for i in r:
        s += [y(i)]
    return s

print(sum(masy(range(10,31,2))))
