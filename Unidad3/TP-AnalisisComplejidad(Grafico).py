import time
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]  # entrada
y = []  # tiempo


def entrega_billetes_2(monto):
    billete = 100
    inc = 0
    billete_actual = billete/(10**inc)
    while (monto > 0):
        if monto >= billete_actual:
            monto = monto-billete_actual
        else:
            inc = inc+1
            billete_actual = billete/(10**inc)


def test_time(a, b, c):
    start = time.time()
    for i in range(a, b, c):
        entrega_billetes_2(i)
    end = time.time()
    y.append(end - start)


test_time(0, 100, 10)
test_time(100, 1000, 100)
test_time(1000, 10000, 1000)
test_time(10000, 100000, 10000)
test_time(100000, 1000000, 100000)

plt.plot(x, y)
plt.xlabel('entradas(n)')
plt.ylabel('tiempo')
plt.show()
