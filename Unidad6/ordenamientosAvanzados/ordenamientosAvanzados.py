from linkedlist import *
import random


def quickSort(L):
    res = LinkedList()
    quickSortR(L, res)
    L.head = None
    current = res.head
    while current != None:
        add(L, current.value)
        current = current.nextNode
    revert(L)


def quickSortR(L, res):
    current = L.head
    if current == None:
        return
    if current.nextNode == None:
        return add(res, current.value)
    # Random Pivot Selection
    pivot = L.head
    for i in range(0, random.randrange(0, length(L)-1)):
        pivot = pivot.nextNode
    # Pivot Sort
    rigthL = LinkedList()
    add(rigthL, pivot.value)
    leftL = LinkedList()
    while current != None:
        if current != pivot:
            if current.value > pivot.value:
                add(rigthL, current.value)
            else:
                add(leftL, current.value)
        current = current.nextNode
    quickSortR(leftL, res)
    quickSortR(rigthL, res)


def mergeSort(L):
    sublist1 = LinkedList()
    sublist2 = LinkedList()
    lengthList = length(L)
    currentNode = L.head
    j = 0

    if lengthList > 1:
        for i in range(0, lengthList):
            if i < lengthList // 2:
                insert(sublist1, currentNode.value, i)
            else:
                insert(sublist2, currentNode.value, j)
                j += 1
            currentNode = currentNode.nextNode

        mergeSort(sublist1)
        mergeSort(sublist2)

        L.head = None
        currentNode1 = sublist1.head
        currentNode2 = sublist2.head
        j = 0
        while currentNode1 != None and currentNode2 != None:
            if currentNode1.value < currentNode2.value:
                insert(L, currentNode1.value, j)
                currentNode1 = currentNode1.nextNode
            else:
                insert(L, currentNode2.value, j)
                currentNode2 = currentNode2.nextNode
            j += 1
        while currentNode1 == None and currentNode2 != None:
            insert(L, currentNode2.value, j)
            currentNode2 = currentNode2.nextNode
            j += 1
        while currentNode2 == None and currentNode1 != None:
            insert(L, currentNode1.value, j)
            currentNode1 = currentNode1.nextNode
            j += 1


test = LinkedList()
add(test, 10)
add(test, 8)
add(test, 9)
add(test, 12)
add(test, 11)
add(test, 15)
add(test, 25)
add(test, 2)

recorrerLista(test)
mergeSort(test)
recorrerLista(test)
