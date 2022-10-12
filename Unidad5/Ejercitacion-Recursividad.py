from linkedlist import *
from mystack import *


def fibonacci(n):
    # Caso Base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Caso General
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def sumaEntero(n):
    if n <= 0:
        return "Error"
    # Caso Base
    if n < 1:
        return 0
    if n == 1:
        return 1
    # Caso General
    else:
        return n + sumaEntero(n-1)


def sumaEnteroPares(n):
    if n % 2 != 0 or n <= 0:
        return "Error"
    # Caso Base
    if n == 2:
        return 2
    else:
        return n + sumaEnteroPares(n-2)


def listOrder(L):
    current = L.head
    count = 0
    while current.nextNode != None:
        if current.value > current.nextNode.value:
            move(L, count + 1, count)
            return listOrder(L)
        current = current.nextNode
        count += 1


def fibonacciStack(n):
    S = LinkedList()
    if n == 0:
        return 0
    if n == 1:
        return 1
    push(S, 1)
    push(S, 1)
    i = 2
    while i <= n:
        num1 = pop(S)
        num2 = pop(S)
        sum = num1 + num2
        push(S, num1)
        push(S, sum)
        i += 1
    return sum
