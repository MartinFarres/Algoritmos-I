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


if len(vect1) == len(vect2):
    prodEscalar = 0
    for i in range(0, len(vect1)):
        prodEscalar += vect1[i] * vect2[i]
    print(f"El producto escalar es {prodEscalar}")
else:
    print("Las dimensiones de los vectores no son iguales")
