from algo1 import *
import math


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
    vect3 = Array(len(vect1), 0)
    norma3 = 0
    for i in range(0, len(vect1)):
        vect3[i] = vect2[i] + vect1[i]
        norma3 += vect3[i]
    norma3 = math.sqrt(norma3)
    print(
        f"El vector resultado es {vect3} con una norma cuadratica de {norma3}")
else:
    print("Las dimensiones de los vectores no son iguales")
