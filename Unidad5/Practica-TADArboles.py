from binarytree import *
from linkedlist import LinkedList


def checkBalanced(R):
    lHeight = getHeight(R.root.leftnode) + 1
    rHeight = getHeight(R.root.rightnode) + 1
    if abs(rHeight - lHeight) <= 1:
        return True
    return False


def getHeight(current):
    height = treeMinHeight(current)
    n = 1
    while current.rightnode != None:
        toCompare = treeMinHeight(current.rightnode, n)
        if height < toCompare:
            height = toCompare
        current = current.rightnode
        n += 1
    return height


def treeMinHeight(current, count=0):
    if current.leftnode == None:
        return count
    else:
        return treeMinHeight(current.leftnode, count+1)


def checkSubTrees(R, S):
    # Determina si hay vacios o son exactamente iguales
    if R == S:
        return True
    if R == None and S == None:
        return True
    if R == None or S == None:
        return False
    # Raiz de S existe en R -> Recorre en preorden apartir de ambos nodos y Compara las listas
    rootS = S.root
    nodeR = searchKey(R, rootS.key)
    if nodeR == None:
        return False
    if nodeR.value != rootS.value:
        return False
    SList = LinkedList()
    RList = LinkedList()
    traverseInPreorderR(rootS, SList)
    traverseInPreorderR(nodeR, RList)
    currentS = SList.head
    currentR = RList.head
    while currentS != None:
        if currentR.value != currentS.value:
            return False
        currentR = currentR.nextNode
        currentS = currentS.nextNode
    return True


def checkBTS(B):
    listB = traverseInOrder(B)
    current = listB.head
    while current.nextNode != None:
        if current.key > current.nextnode.key:
            return False
        current = current.nextNode
    return True


test = BynaryTree()
insert(test, "10", 10)
insert(test, "8", 8)
insert(test, "9", 9)
insert(test, "12", 12)
insert(test, "11", 11)
insert(test, "15", 15)
insert(test, "25", 25)
insert(test, "2", 2)


test2 = BynaryTree()
insert(test2, "8", 8)
insert(test2, "9", 9)
insert(test2, "2", 2)

print(checkSubTrees(test, test2))
