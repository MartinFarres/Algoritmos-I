from algo1 import *


def search(Array, element):
    for i in range(0, len(Array)):
        if Array[i] == element:
            return i
    return None


def insert(Array, element, position):
    if position <= len(Array):
        for i in range(len(Array) - 1, position - 1, -1):
            if i == position:
                Array[i] = element
            else:
                Array[i] = Array[i - 1]
        return position
    else:
        return None


def delete(Array, element):
    position = search(Array, element)
    if position != None:
        for i in range(position, len(Array)):
            if i != len(Array) - 1:
                Array[i] = Array[i + 1]
            else:
                Array[i] = None
    return position


def length(Array):
    res = 0
    for i in range(0, len(Array)):
        if Array[i] != None:
            res += 1
    return res
