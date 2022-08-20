from algo1 import *
import math

lenVector = input_int("Ingrese la dimension del vector: ")
vector = Array(lenVector, 0)
for i in range(0, lenVector):
    vector[i] = input_int(f"Ingrese el valor del {i + 1}° elemento: ")

def maxAbs(arr):
    maxNum = 0
    for i in range(0, len(arr)):
        maxNum = abs(arr[i]) > maxNum and abs(arr[i]) or maxNum
    print(maxNum)

maxAbs(vector)