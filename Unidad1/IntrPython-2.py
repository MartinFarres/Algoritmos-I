from algo1 import *
import myLib

arrNums = Array(3, 0)
for i in range(0, 3):
    num = myLib.valInt("Ingrese un valor entero: ", 0)
    arrNums[i] = num


def compararVal(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    print(arr)


def promedioVal(arr):
    print((arr[0] + arr[-1])/2)


compararVal(arrNums)
promedioVal(arrNums)
