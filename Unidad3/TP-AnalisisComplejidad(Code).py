import time


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
    return end - start


totalTime = test_time(0, 100, 10)
totalTime += test_time(100, 1000, 100)
totalTime += test_time(1000, 10000, 1000)
totalTime += test_time(10000, 100000, 10000)
totalTime += test_time(100000, 1000000, 100000)

print(totalTime)
