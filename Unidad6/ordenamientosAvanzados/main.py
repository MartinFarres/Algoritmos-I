# Implementacion de un binary heap
# Algoritmos y estructuras de datos I
# Ingenieria - Uncuyo
# harpomaxx@gmail.com
# jue oct 26 09:24:47 ART 2017

# Ejercitacion: Implementar las operaciones y las porciones de codigo faltantes

import linkedlist
import myqueue
from random import randint


class Bheap:
    """ Estructura Bheap, lo unico que tiene una referencia a un lista.
    """
    bheaplist = linkedlist.LinkedList()

    def __str__(self):
        """ Permite hacer un print a una estructura Bheap
        """
        str_list = ""
        current = self.bheaplist.head.nextNode
        while current != None:
            str_list = str_list+str(current.value)+" "
            current = current.nextNode
        return (str_list)


def delMax(BH):
    """ Recupera el mayor elemento del heap. Este siempre se encontrara al comienzo (posicion 1).
        Para manter la esctrucura del arbol binario se reemplaza el nodo raiz por el ultimo nodo.

        Luego mediante la funcion shiftDown se va recorriendo el arbol hasta encontrar la posicion 
        correcta de dicho nodo. De esta manara se garantiza la propiedad heap.
    """

    if linkedlist.length(BH.bheaplist) > 1:
        retval = linkedlist.access(BH.bheaplist, 1)
        value = myqueue.dequeue(BH.bheaplist)
        linkedlist.update(BH.bheaplist, value, 1)
        shiftDown(BH, 1)
    return retval


def shiftUp(BH, i):
    """ Recorre el arbol desde los nodos hacia la raiz y va reemplazando el nodo i por su padre
        siempre y cuando i sea mayor. La operacion matematica i // 2 nos permite rapidamente encontrar al padre.
    """
    while i // 2 > 0:
        childValue = linkedlist.access(BH.bheaplist, i)
        parentValue = linkedlist.access(BH.bheaplist, i // 2)
        if childValue > parentValue and childValue != None:
            linkedlist.update(BH.bheaplist, childValue, i // 2)
            linkedlist.update(BH.bheaplist, parentValue, i)
        else:
            return
        i = i // 2
        shiftUp(BH, i)


def shiftDown(BH, i, currentsize=None):
    """ Recorre el arbol desde la raiz y  hacia los nodos (arriba hacia abajo) va reemplazando el nodo i por sus hijos
        siempre y cuando alguno de sus hijos sea mayor. 
    """
    if currentsize == None:
        currentsize = linkedlist.length(BH.bheaplist)-1
    while (i * 2) <= currentsize:
        mc = maxChild(BH, i, currentsize)
        mcValue = linkedlist.access(BH.bheaplist, mc)
        currentValue = linkedlist.access(BH.bheaplist, i)
        if mcValue > currentValue and mcValue != None:
            linkedlist.update(BH.bheaplist, mcValue, i)
            linkedlist.update(BH.bheaplist, currentValue, mc)
        i = mc
        shiftDown(BH, i)


def maxChild(BH, i, currentsize):
    """ Determina dado un nodo i, cual de sus hijos es el mayor y devuelve la posicion 
    """
    if i * 2 + 1 > currentsize:
        return i * 2
    else:
        if linkedlist.access(BH.bheaplist, i*2) > linkedlist.access(BH.bheaplist, i*2+1):
            return i * 2
        else:
            return i * 2 + 1


def insert(BH, k):
    """ Inserta un elemento en el heap. Si la lista esta vacia, se crea un elemento 0. Este ultimo no se utiliza,
        pero facilita las operaciones matematicas para acceder a los padres e hijos. 
    """
    pos = linkedlist.length(BH.bheaplist)
    if pos == 0:
        linkedlist.add(H.bheaplist, 0)
        pos = pos+1
    linkedlist.insert(BH.bheaplist, k, pos)
    currentsize = linkedlist.length(BH.bheaplist)-1
    shiftUp(BH, currentsize)


def heapify(BH, L):
    """ Dada una lista crea un heap con complejidad temporal O(n)

    """
    i = linkedlist.length(L) // 2
    BH.bheaplist.head = L.head
    linkedlist.add(BH.bheaplist, 0)
    while (i > 0):
        shiftDown(BH, i)
        i = i - 1


def length(BH):
    return linkedlist.length(BH.bheaplist)-1


if __name__ == "__main__":
    H = Bheap()
    insert(H, 8)
    insert(H, 1)
    insert(H, 5)
    insert(H, 4)
    print(H)
    minimun = delMax(H)
    print(H)
    print("----")
    L = linkedlist.LinkedList()
    linkedlist.add(L, 4)
    linkedlist.add(L, 3)
    linkedlist.add(L, 2)
    linkedlist.add(L, 1)
    linkedlist.add(L, 12)
    linkedlist.add(L, 255)
    linkedlist.add(L, 1000)
    linkedlist.recorrerLista(L)
    heapify(H, L)
    print(H)
