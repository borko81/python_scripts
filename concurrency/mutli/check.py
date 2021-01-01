import multiprocessing
import random
import time


def generate_random(t):
    num = random.random()
    time.sleep(t)
    print(num)


def main_for_generate_random():
    p1 = time.perf_counter()
    process = [multiprocessing.Process(target=generate_random, args=()) for _ in range(5)]

    for x in process:
        x.start()

    for x in process:
        x.join()

    print(round(time.perf_counter() - p1, 2), "time")


def main_with_pool():
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    result = pool.map(generate_random, [1, 2, 1])
    return result

if __name__ == '__main__':
    main_with_pool()

