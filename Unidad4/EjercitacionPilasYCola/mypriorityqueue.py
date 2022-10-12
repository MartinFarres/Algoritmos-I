from linkedlist import *
from mystack import *


class PriorityQueue:
    head = None


class PriorityNode:
    value = None
    nextNode = None
    priority = None


def enqueue_priority(Q, element, priority):
    newNode = PriorityNode()
    newNode.value = element
    newNode.priority = priority
    position = 0
    if Q.head == None:
        Q.head = newNode
        return position

    current = Q.head
    if current.priority <= priority:
        newNode.nextNode = current
        Q.head = newNode
        return position

    while current.nextNode != None:
        if current.nextNode.priority >= priority:
            current = current.nextNode
        else:
            newNode.nextNode = current.nextNode
            current.nextNode = newNode
            return position
        position += 1
    current.nextNode = newNode
    position += 1
    return position


def dequeue_priority(Q):
    return pop(Q)
