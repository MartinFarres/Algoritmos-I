from operator import getitem
from algo1 import *


def cargaVector(n):
    lenVector = input_int(f"Ingrese la dimension del {n}° vector: ")
    vector = Array(lenVector, 0)
    for i in range(0, lenVector):
        vector[i] = input_int(
            f"Ingrese el valor del {i + 1}° elemento del {n}° Vector: ")
    return vector


vect1 = cargaVector(1)
vect2 = cargaVector(2)

dif = ""
for i in vect1:
    if i not in vect2:
        dif += str(i)
for i in vect2:
    if i not in vect1:
        dif += str(i)
print(dif)
