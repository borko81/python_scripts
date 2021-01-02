import multiprocessing
import time

NUMBERS = 50000, 50001, 50002, 50003


def factorial(n):
    "Take a while for a large numbers"

    print("Start for number {}".format(n))
    f = 1
    for i in range(1, n + 1):
        f *= i
    print("Done number {}".format(n))
    return f


# Single process
def with_single():
    t1 = time.perf_counter()
    result = []
    for n in NUMBERS:
        result.append(factorial(n))
    print(time.perf_counter() - t1)


# With map
def with_map():
    t1 = time.perf_counter()
    result = list(map(factorial, NUMBERS))
    print(time.perf_counter() - t1)


# with Pool
def with_pool():
    t1 = time.perf_counter()
    with multiprocessing.Pool() as pool:
        result = pool.map(factorial, NUMBERS)
    print(time.perf_counter() - t1)


if __name__ == '__main__':
    with_pool()
