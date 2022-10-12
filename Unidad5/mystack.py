from linkedlist import *


def push(S, element):
    add(S, element)


def pop(S):
    current = S.head
    if current != None:
        newNode = current.nextNode
        S.head = newNode
        current.nextNode = None
        return current.value
    return
