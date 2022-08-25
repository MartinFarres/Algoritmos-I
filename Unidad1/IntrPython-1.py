from algo1 import *
import myLib

num1 = myLib.valInt("Ingrese un valor entero: ", 0)
num2 = myLib.valInt("Ingrese otro valor entero: ", 0)
listado = Array(num1 + num2, 0)


def listDecreciente(arr):
    for i in range(len(arr), 0, -5 if len(arr) > 50 else -2):
        print(i, ', ', end='')


listDecreciente(listado)
