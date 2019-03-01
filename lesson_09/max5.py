# max5.py
def max_sequence(seq):
    """
    Функция ищет пять соседних элементов списка, сумма значений которых максимальна.
    >>> max_sequence([1, 3, 1, 1, 4, 4, 3, 1, 4, 4, 4, 3, 4, 4, 1, 3, 2, 4, 4, 4])
    [4, 4, 4, 3, 4]
    >>> max_sequence([1, 5, 7, 2, 9, 2, 9, 2, 5, 3, 7, 6, 3, 3, 7, 4, 4, 1, 9, 5])
    [7, 2, 9, 2, 9]
    """
    s = sum(seq[:5])
    ma = 0
    ms = s
    for i in range(1,len(seq)-5):
        s = sum(seq[i:i+5])
        if s > ms:
            ma = i
            ms = s
    return seq[ma: ma+5]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
