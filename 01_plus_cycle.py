from itertools import cycle


def ex1(n):
    new_n = n
    cycle = 0

    while True:
        x = int(str(new_n)[0])
        y = int(str(new_n)[-1])
        plus = x + y
        new_n = str(y) + str(plus)[-1]
        if int(new_n) == n:
            print(cycle)
            break
        cycle += 1

def ex2(n):
    new_n = n
    cycle = 0

    while True:
        x = new_n // 10
        y = new_n % 10
        z = (x + y) % 10
        new_n = x * 10 + z
        if new_n == n:
            print(cycle)
            break
        cycle += 1

ex2(55)
ex1(55)