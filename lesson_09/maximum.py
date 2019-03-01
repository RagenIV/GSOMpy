# maximum.py

def maximum(*num):
    """
    >>> maximum(3, 2, 8)
    8
    >>> maximum(1, 5, 9, -2, 2)
    9
    >>> maximum()    
    """
    if len(num) > 0:
        res = num[0]
        for i in num:
            if i > res:
                res = i
        return res

if __name__ == '__main__':
    import doctest
    doctest.testmod()
