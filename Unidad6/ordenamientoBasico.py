from linkedlist import *


def BubbleSort(R):
    for i in range(length(R)):
        current = R.head
        n = 0
        while current.nextNode != None:
            if current.value > current.nextNode.value:
                move(R, n, n+1)
            else:
                current = current.nextNode
            n += 1


def selectionSort(R):
    for i in range(length(R)):
        # Encontrar el mínimo elemento en el resto de la lista desordenada
        minPos = i
        for j in range(i+1, length(R)):
            if access(L, minPos) > access(R, j):
                minPos = j
        # Intercambiar el elemento
        move(R, minPos, i)


def insertionSort(R):
    for i in range(length(R)):
        posOrigin = i
        for j in range(0, i):
            if access(R, posOrigin) < access(R, j):
                move(R, posOrigin, j)


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
insertionSort(test)
recorrerLista(test)
