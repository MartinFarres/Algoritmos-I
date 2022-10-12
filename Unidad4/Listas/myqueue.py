from linkedlist import *


def enqueue(Q, element):
    add(Q, element)


def dequeue(Q):
    if Q.head != None:
        pos = length(Q) - 1
        element = access(Q, pos)
        delete(Q, element)
        return element
    return
