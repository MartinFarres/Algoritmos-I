from algo1 import *

num1 = input_int("Ingrese un valor entero: ")
num2 = input_int("Ingrese otro valor entero: ")
listado = Array(num1 + num2, 0)

def listDecreciente(arr):
    for i in range(len(arr), 0, -5 if len(arr) > 50 else -2):
        print(i,', ', end='')

listDecreciente(listado)