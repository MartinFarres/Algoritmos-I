from algo1 import *
import math


def cargaMatriz():
    cantFilas = input_int(f"Ingrese la cantidad de filas de la matriz: ")
    cantCol = input_int(f"Ingrese la cantidad de columnas de la matriz: ")
    matriz = Array(cantFilas, Array(cantCol, 0))
    for i in range(0, cantFilas):
        for j in range(0, cantCol):
            matriz[i][j] = input_int(
                f"Ingrese el valor del elemento {i + 1}x{j + 1} de la Matriz: ")
    return matriz


def MTS(matr):
    if len(matr) == len(matr[0]):
        res = True
        for i in range(0, len(matr[0])):
            for j in range(0, len(matr)):
                if i > j and matr[i][j] != 0:
                    res = False
    else:
        res = False
    return res


def detMTS(matr):
    det = 1
    for i in range(0, len(matr[0])):
        for j in range(0, len(matr)):
            if i == j:
                det = det * matr[i][j]
    return det


matriz1 = cargaMatriz()
print(detMTS(matriz1)) if MTS(matriz1) else print("No es una MTS")
