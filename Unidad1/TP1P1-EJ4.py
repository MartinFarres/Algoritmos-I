from algo1 import *
import math


def cargaMatriz(n):
    cantFilas = input_int(f"Ingrese la cantidad de filas de la matriz {n}: ")
    cantCol = input_int(f"Ingrese la cantidad de columnas de la matriz {n}: ")
    matriz = Array(cantFilas, Array(cantCol, 0))
    for i in range(0, cantFilas):
        for j in range(0, cantCol):
            matriz[i][j] = input_int(
                f"Ingrese el valor del elemento {i + 1}x{j + 1} de la Matriz {n}: ")
    return matriz


matriz1 = cargaMatriz(1)
matriz2 = cargaMatriz(2)

if len(matriz1[0]) == len(matriz2[0]) and len(matriz1) == len(matriz2):
    matriz3 = Array(len(matriz1), Array(len(matriz1[0]), 0))
    for i in range(0, len(matriz1[0])):
        for j in range(0, len(matriz1)):
            matriz3[i][j] = matriz1[i][j] - matriz2[i][j]
            print(matriz3[i][j])
else:
    print("Dimensiones Incorrectas")
