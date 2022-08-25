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


def prodMatr(matriz1, matriz2):
    if len(matriz1[0]) == len(matriz2):
        matriz3 = Array(len(matriz1[0]), Array(len(matriz2), 0))
        for i in range(0, len(matriz1)):
            for j in range(0, len(matriz2[0])):
                for k in range(0, len(matriz1)):
                    if matriz3[i][j] == None:
                        matriz3[i][j] = 0
                    matriz3[i][j] += matriz1[i][k] * matriz2[k][j]
                print(matriz3[i][j])
        return matriz3
    else:
        print("Dimensiones Incorrectas")
        return None


def diagDominante(matriz):
    res = True
    for i in range(0, len(matriz)):
        if i != 0 and sumFila > diagonal:
            res = False
        sumFila = 0  # Suma de los elementos de la fila i != j
        diagonal = 0  # Elemento de la diagonal
        for j in range(0, len(matriz[0])):
            if i == j:
                diagonal = abs(matriz[i][j])
            else:
                sumFila += abs(matriz[i][j])
    return res


matriz1 = cargaMatriz(1)
matriz2 = cargaMatriz(2)
matriz3 = prodMatr(matriz1, matriz2)
matriz3 != None and print(diagDominante(matriz3))
