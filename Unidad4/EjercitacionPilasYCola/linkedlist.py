class LinkedList:
    head = None


class Node:
    value = None
    nextNode = None


def add(L, element):
    newNode = Node()
    newNode.value = element
    if L.head == None:
        L.head = newNode
    else:
        newNode.nextNode = L.head
        L.head = newNode


def search(L, element):
    currentNode = L.head
    position = 0
    while currentNode != None:
        if currentNode.value == element:
            return position
        position += 1
        currentNode = currentNode.nextNode
    return


def insert(L, element, position):
    current = L.head
    currentPos = 0

    if position == 0:
        add(L, element)
        return position

    elif position > 0:
        if current == None:
            return
        newNode = Node()
        newNode.value = element

        while current.nextNode != None:
            if currentPos + 1 != position:
                current = current.nextNode
                currentPos += 1
            else:
                newNode.nextNode = current.nextNode
                current.nextNode = newNode
                return position
        current.nextNode = newNode
        return currentPos + 1
    return


def length(L):
    currentNode = L.head
    len = 0
    while currentNode != None:
        len += 1
        currentNode = currentNode.nextNode
    return len


def delete(L, element):
    position = search(L, element)
    if position == None:
        return
    currentNode = L.head
    if position == 0:
        L.head = currentNode.nextNode
        return
    for i in range(0, position - 1):
        currentNode = currentNode.nextNode
    currentNode.nextNode = currentNode.nextNode.nextNode
    return position


def access(L, position):
    len = length(L)
    currentNode = L.head
    if len > 0 and position <= (len - 1):
        for i in range(0, position):
            currentNode = currentNode.nextNode
        return currentNode.value


def update(L, element, position):
    current = L.head
    if position >= 0:
        i = 0
        while current != None and i <= position - 1:
            current = current.nextNode
            i += 1
        if current == None:
            return
        current.value = element
        return position
    return


def recorrerLista(S):
    current = S.head
    while current != None:
        print(current.value)
        current = current.nextNode
