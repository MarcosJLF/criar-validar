from config import ALPHABET, NUMBER, CARACTER
import random


def insert_all(n):
    c = 0
    n = n - 4
    arr = []
    while c < n:
        c += 1
        for i in range( n // 2):
            c += 1
            l = random.choice(ALPHABET)
            arr.append(l)
       
        nu = random.choice(NUMBER)
        arr.append(nu)

        ca = random.choice(CARACTER)
        arr.append(ca)

    f = []
    f = string(arr)

    return f

def string(lista):

    new_list = "".join([str(x) for x in lista])
    return new_list