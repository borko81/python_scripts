import time
import random
from multiprocessing import Process


procs = []


def calculate_prime(n):
    check = n
    primefac = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primefac.append(d)
            n //= d
        d += 1
    if n > 1:
        primefac.append(n)
    return(check, primefac)


t0 = time.time()


def execute():
    for i in range(10000):
        rand = random.randint(200000, 1000000)
        print(calculate_prime(rand))


if __name__ == '__main__':
    for i in range(3):
        proc = Process(target=execute, args=())
        procs.append(proc)
        proc.start()

    t1 = time.time()
    total_time = t1 - t0
    print(total_time)
