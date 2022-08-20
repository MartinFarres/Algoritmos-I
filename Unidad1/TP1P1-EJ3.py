from algo1 import *
import math


def cargaVector():
    lenVector = input_int(f"Ingrese la dimension del vector: ")
    vector = Array(lenVector, 0)
    for i in range(0, lenVector):
        vector[i] = input_int(
            f"Ingrese el valor del {i + 1}° elemento del Vector: ")
    return vector


def cargaMatriz():
    cantFilas = input_int(f"Ingrese la cantidad de filas de la matriz: ")
    cantCol = input_int(f"Ingrese la cantidad de columnas de la matriz: ")
    matriz = Array(cantFilas, Array(cantCol, 0))
    for i in range(0, cantFilas):
        for j in range(0, cantCol):
            matriz[i][j] = input_int(
                f"Ingrese el valor del elemento {i + 1}x{j + 1} de la Matriz: ")
    return matriz


vect = cargaVector()
matriz = cargaMatriz()

if len(matriz[0]) == len(vect):
    vect2 = Array(len(vect), 0)
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[0])):
            if vect2[i] == None:
                vect2[i] = 0
            vect2[i] += matriz[i][j] * vect[j]
    print(
        f"El vector resultado es {vect2}")
else:
    print("Dimensiones Incorrectas")
