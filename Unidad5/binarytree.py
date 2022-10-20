from linkedlist import *


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

# Delete -----------------------------------------------------------------------------


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


# -------------------------------------------------------------------------------------------


def treeMin(current):
    if current.leftnode == None:
        return current
    else:
        return treeMin(current.leftnode)


test = BynaryTree()
insert(test, "10", 10)
insert(test, "8", 8)
insert(test, "9", 9)
insert(test, "12", 12)
insert(test, "11", 11)
insert(test, "15", 15)
insert(test, "25", 25)
insert(test, "2", 2)

print(search(test, "11"))
print(delete(test, "11"))
print(search(test, "12"))
print(search(test, "11"))
