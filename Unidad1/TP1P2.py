from logging import exception
from msilib.schema import Error
from algo1 import *


def Create_Set(arr):
    n = 0
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j] and arr[i] != None:
                arr[j] = None
                n += 1
    TDASet = Array(len(arr)-n, 0)
    j = 0
    for i in range(0, len(arr)):
        if arr[i] != None:
            TDASet[j] = arr[i]
            j += 1
    return TDASet


def Check_Duplicates(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                raise Exception("Error Set con duplicados")
    return True


def Union(arr1, arr2):
    Check_Duplicates(arr1)
    Check_Duplicates(arr2)
    unionStr = ""
    for i in arr1:
        if i in arr2:
            unionStr += str(i)
    for i in arr2:
        if i in arr1:
            unionStr += str(i)
    unionArr = Array(len(unionStr), 0)
    for i in range(0, len(unionArr)):
        unionArr[i] = int(unionStr[i])
    return unionArr


def Intersection(arr1, arr2):
    Check_Duplicates(arr1)
    Check_Duplicates(arr2)
    interStr = ""
    for i in range(0, len(arr1)):
        for j in range(0, len(arr2)):
            if arr1[i] == arr2[j]:
                interStr += str(arr1[i])
    interArr = Array(len(interStr), 0)
    for i in range(0, len(interArr)):
        interArr[i] = int(interStr[i])
    return interArr


def Difference(arr1, arr2):
    Check_Duplicates(arr1)
    Check_Duplicates(arr2)
    diffStr = ""
    for i in arr1:
        if i not in arr2:
            diffStr += str(i)
    for i in arr2:
        if i not in arr1:
            diffStr += str(i)
    difArr = Array(len(diffStr), 0)
    for i in range(0, len(difArr)):
        difArr[i] = int(diffStr[i])
    return difArr


p = Difference([0, 1, 2], [1, 5])
print(p)
