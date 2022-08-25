from algo1 import *


def cargaMatriz(n=1):
    cantFilas = input_int(f"Ingrese la cantidad de filas de la matriz {n}: ")
    cantCol = input_int(f"Ingrese la cantidad de columnas de la matriz {n}: ")
    matriz = Array(cantFilas, Array(cantCol, 0))
    for i in range(0, cantFilas):
        for j in range(0, cantCol):
            matriz[i][j] = input_int(
                f"Ingrese el valor del elemento {i + 1}x{j + 1} de la Matriz {n}: ")
    return matriz


def MTI(matr):
    res = False
    if len(matr) == len(matr[0]):
        res = True
        for i in range(0, len(matr)):
            for j in range(0, len(matr[0])):
                if i < j and matr[i][j] != 0:
                    res = False
    return res


def transponerMatr(matriz):
    matrizT = Array(len(matriz[0]), Array(len(matriz), 0))
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[0])):
            matrizT[j][i] = matriz[i][j]
    return matrizT


matriz = cargaMatriz()
if MTI(matriz):
    matrizT = transponerMatr(matriz)
