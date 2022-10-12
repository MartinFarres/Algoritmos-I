from linkedlist import *
from myqueue import *
from mystack import *

# Ejercicio1


def Ejercicio1():
    listA = LinkedList()
    add(listA, 678)
    add(listA, 3)
    add(listA, 22)
    add(listA, 54)
    add(listA, 345)
    add(listA, 89)
    add(listA, 67)
    add(listA, 3)
    add(listA, 45)
    add(listA, 24)
    print("Lista A: ")
    recorrerLista(listA)

    listB = LinkedList()
    add(listB, 33)
    add(listB, 12)
    add(listB, 567)
    add(listB, 234)
    add(listB, 15)
    add(listB, 12)
    add(listB, 59)
    add(listB, 64)
    add(listB, 34)
    add(listB, 46)
    print("Lista B: ")
    recorrerLista(listB)

    listC = LinkedList()
    addFromA = False
    lenA = length(listA)
    lenB = length(listB)
    lenC = lenA + lenB

    for i in range(lenC):
        lenC -= 1
        if addFromA:
            current = listA.head
            len = lenA
            lenA -= 1
        else:
            current = listB.head
            len = lenB
            lenB -= 1

        for j in range(len-1):
            current = current.nextNode
        if current != None:
            add(listC, current.value)
        addFromA = not addFromA

    print("Lista C: ")
    recorrerLista(listC)

    current = listC.head
    while current != None:
        if current.value % 2 == 0:
            delete(listC, current.value)
        current = current.nextNode.nextNode

    print("Lista C actualizada: ")
    recorrerLista(listC)

    listD = LinkedList()
    current = listC.head
    while current != None:
        if current.value % 2 != 0:
            add(listD, current.value)
        current = current.nextNode

    listD = revert(listD)
    print("Lista D: ")
    recorrerLista(listD)

    current = listA.head
    while current != None:
        current2 = listA.head
        while current2.nextNode != None:
            if current.value == current2.nextNode.value and current != current2.nextNode:
                current2.nextNode = current2.nextNode.nextNode
            current2 = current2.nextNode
        current = current.nextNode

    listA = revert(listA)
    current = listB.head
    while current != None:
        if current.value >= 50 and current.value <= 100:
            add(listA, current.value)
        current = current.nextNode

    listA = revert(listA)
    print("Lista A actualizada: ")
    recorrerLista(listA)

# Ejercicio2


class Empleado:
    nombre = None
    edad = None
    nroLegajo = None


def print_list_E(L):
    current = L.head
    currentPos = 0

    while current != None:
        if currentPos != 0:
            print(" ↓ ")
        print(current.value.nombre, end=", ")
        print(current.value.edad, end=", ")
        print(current.value.nroLegajo)
        current = current.nextNode
        currentPos += 1
    print()
    return currentPos


empleados = LinkedList()
empleado = Empleado()

empleado.nombre = "Luis Esteban"
empleado.edad = 32
empleado.nroLegajo = 7
add(empleados, empleado)

empleado = Empleado()
empleado.nombre = "Eduardo Ángel"
empleado.edad = 34
empleado.nroLegajo = 2
add(empleados, empleado)

empleado = Empleado()
empleado.nombre = "Pedro César"
empleado.edad = 45
empleado.nroLegajo = 8
add(empleados, empleado)

empleado = Empleado()
empleado.nombre = "Luis Esteban"
empleado.edad = 32
empleado.nroLegajo = 7
add(empleados, empleado)

empleado = Empleado()
empleado.nombre = "Pedro Augusto"
empleado.edad = 40
empleado.nroLegajo = 9
add(empleados, empleado)

empleado = Empleado()
empleado.nombre = "Juan Carlos"
empleado.edad = 23
empleado.nroLegajo = 5
add(empleados, empleado)

empleado = Empleado()
empleado.nombre = "Luis Esteban"
empleado.edad = 32
empleado.nroLegajo = 7
add(empleados, empleado)

empleado = Empleado()
empleado.nombre = "Juan Carlos"
empleado.edad = 23
empleado.nroLegajo = 5
add(empleados, empleado)

empleado = Empleado()
empleado.nombre = "Eduardo Ángel"
empleado.edad = 34
empleado.nroLegajo = 2
add(empleados, empleado)


def Ejercicio2():
    print_list_E(empleados)


# Ejercicio 3

def searchE(L, nroLegajo):
    current = L.head
    currentPos = 0

    while current != None:
        if current.value.nroLegajo == nroLegajo:
            return currentPos

        current = current.nextNode
        currentPos += 1
    return


def Ejercicio3():
    empleados = LinkedList()
    empleado = Empleado()

    current = empleados.head
    while current != None:
        current2 = empleados.head

        while current2.nextNode != None:
            if current.value.nroLegajo == current2.nextNode.value.nroLegajo and current != current2.nextNode:
                current2.nextNode = current2.nextNode.nextNode
            if current2.nextNode != None:
                current2 = current2.nextNode
        current = current.nextNode

    print()
    print("Lista sin repetidos: ")
    print_list_E(empleados)

    empleado = Empleado()
    empleado.nombre = "Ernesto Andrés"
    empleado.edad = 55
    empleado.nroLegajo = 6

    insert(empleados, empleado, searchE(empleados, 7))
    print()
    print("Agregar antes del legajo número 7 el siguiente: Ernesto Andrés, 55, 6")
    print_list_E(empleados)

    current = empleados.head
    currentPos = 0

    while current.nextNode != None:
        if current.nextNode.value.nroLegajo == 9:
            node9 = Node()
            node9.value = current.nextNode.value

            current.nextNode = current.nextNode.nextNode
            current.nextNode.nextNode = node9
            break

        current = current.nextNode
        currentPos += 1

    print()
    print("Mover el legajo 9 luego del legajo 8")
    print_list_E(empleados)
