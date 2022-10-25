from linkedlist import *
from myqueue import *


class BynaryTree:
    root = None


class BynaryTreeNode:
    key = None
    value = None
    leftnode = None
    rightnode = None
    parent = None


def insert(B, element, key):
    current = B.root
    newNode = BynaryTreeNode()
    newNode.key = key
    newNode.value = element
    if current == None:
        B.root = newNode
        return key
    insertR(newNode, B.root)


def insertR(newNode, current):
    if newNode.key > current.key:
        if current.rightnode == None:
            current.rightnode = newNode
            newNode.parent = current
            return newNode.key
        insertR(newNode, current.rightnode)
    elif newNode.key < current.key:
        if current.leftnode == None:
            current.leftnode = newNode
            newNode.parent = current
            return newNode.key
        insertR(newNode, current.leftnode)
    else:
        return None


def search(B, element):
    current = B.root
    if current.value == element:
        return current.key
    if current == None:
        return None
    try:
        return searchR(current, element).key
    except:
        return


def searchR(node, element):
    if node == None:
        return
    if node.value == element:
        return node
    right = searchR(node.rightnode, element)
    if right != None:
        return right
    left = searchR(node.leftnode, element)
    if left != None:
        return left


def searchKey(B, key):
    current = B.root
    if current.key == key:
        return current
    if current == None:
        return
    return searchKeyR(current, key)


def searchKeyR(node, key):
    if node.key == key:
        return node
    if node.key > key:
        if node.leftnode != None:
            return searchKeyR(node.leftnode, key)
        return
    else:
        if node.rightnode != None:
            return searchKeyR(node.rightnode, key)
        return


def delete(B, element):
    current = B.root
    if current.value == element:
        nodeToDel = current
    if current == None:
        return None
    nodeToDel = searchR(current, element)
    # Node NO LEFT Child
    if nodeToDel.leftnode == None:
        transplant(B, nodeToDel, nodeToDel.rightnode)  # Subo el nodo derecho
    # Node NO RIGHT Child
    elif nodeToDel.rightnode == None:
        transplant(B, nodeToDel, nodeToDel.leftnode)  # Subo el nodo izquierdo
    # Node HAS 2 CHILDREN
    else:
        # Buscamos el menor de la rama de los mayores (no tiene leftnode)
        y = treeMin(nodeToDel.rightnode)
        if y.parent != nodeToDel:  # El padre del menor no es "nodeToDel"
            # Nueva subrama con "Y" mayor, "nodeToDel.right" al derecho de "Y", e "Y.right" al izquierdo de "nodeToDel.right"
            transplant(B, y, y.rightnode)
            y.rightnode = nodeToDel.rightnode
            y.rightnode.parent = y
        # Remplazo "Y" con "nodeToDel"
        transplant(B, nodeToDel, y)
        y.leftnode = nodeToDel.leftnode
        y.leftnode.parent = y
    return nodeToDel.key


def transplant(B, current, new):
    # Transplanta el nodo 'Current' con el nuevo nodo 'New'
    if current.parent == None:
        B.root = current
    elif current == current.parent.leftnode:
        current.parent.leftnode = new
    else:
        current.parent.rightnode = new
    if new != None:
        new.parent = current.parent


def deleteKey(B, key):
    current = searchKey(B, key)
    if current == None:
        return
    if current.leftnode == None:
        transplant(B, current, current.rightnode)
    elif current.rightnode == None:
        transplant(B, current, current.leftnode)
    else:
        nodeMin = treeMin(current.rightnode)
        if nodeMin.parent != current:
            transplant(B, nodeMin, nodeMin.rightnode)
            nodeMin.rightnode = current.rightnode
            nodeMin.parent.rightnode = nodeMin
        transplant(B, current, nodeMin)
        nodeMin.leftnode = current.leftnode
        nodeMin.leftnode.parent = nodeMin
    return current.key


def access(B, key):
    current = searchKey(B, key)
    if current == None:
        return
    return current.value


def update(B, element, key):
    current = searchKey(B, key)
    if current == None:
        return
    current.value = element
    return current.key


def treeMin(current):
    if current.leftnode == None:
        return current
    else:
        return treeMin(current.leftnode)


def traverseInOrder(B):
    if B == None:
        return None
    R = LinkedList()
    traverseInOrderR(B.root, R)
    return revert(R)


def traverseInOrderR(current, R):
    if current != None:
        traverseInOrderR(current.leftnode, R)
        add(R, current.value)
        traverseInOrderR(current.rightnode, R)


def traverseInPreorder(B):
    if B == None:
        return None
    R = LinkedList()
    traverseInPreorderR(B.root, R)
    return revert(R)


def traverseInPreorderR(current, R):
    if current != None:
        add(R, current.value)
        traverseInPreorderR(current.leftnode, R)
        traverseInPreorderR(current.rightnode, R)


def traverseInPostorder(B):
    if B == None:
        return None
    R = LinkedList()
    traverseInPostorderR(B.root, R)
    return revert(R)


def traverseInPostorderR(current, R):
    if current != None:
        traverseInPostorderR(current.leftnode, R)
        traverseInPostorderR(current.rightnode, R)
        add(R, current.value)


def traverseBreadFirst(B):
    queue = LinkedList()
    valuesQueue = LinkedList()
    enqueue(queue, B.root)
    while queue.head != None:
        node = dequeue(queue)
        enqueue(valuesQueue, node.value)

        if node.leftnode != None:
            enqueue(queue, node.leftnode)
        if node.rightnode != None:
            enqueue(queue, node.rightnode)
    return revert(valuesQueue)


test = BynaryTree()
insert(test, "10", 10)
insert(test, "8", 8)
insert(test, "9", 9)
insert(test, "12", 12)
insert(test, "11", 11)
insert(test, "15", 15)
insert(test, "25", 25)
insert(test, "2", 2)

inOrder = traverseInOrder(test)
preOrder = traverseInPreorder(test)
postOrder = traverseInPostorder(test)
amplOrder = traverseBreadFirst(test)

recorrerLista(inOrder)
recorrerLista(preOrder)
recorrerLista(postOrder)
recorrerLista(amplOrder)
