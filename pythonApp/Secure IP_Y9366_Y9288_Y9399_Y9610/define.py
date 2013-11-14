def rotate_left(x, n):
    "Rotate x (32 bit) left n bits circularly."

    return (x << n) | (x >> (32-n))


def XX(func, a, b, c, d, x, s, ac):

    res = 0L
    res = res + a + func(b, c, d)
    res = res + x 
    res = res + ac
    res = res & 0xffffffffL
    res = rotate_left(res, s)
    res = res & 0xffffffffL
    res = res + b

    return res & 0xffffffffL


def decode(list):
    "Transforms a list of characters into a list of longs."

    imax = len(list)/4
    hl = [0L] * imax

    j = 0
    i = 0
    while i < imax:
        b0 = long(ord(list[j])) # "ord" takes as input one char and returns the corresponding ASCII value
        b1 = (long(ord(list[j+1]))) << 8 # shift left
        b2 = (long(ord(list[j+2]))) << 16
        b3 = (long(ord(list[j+3]))) << 24
        hl[i] = b0 | b1 |b2 | b3
        i = i+1
        j = j+4

    return hl
