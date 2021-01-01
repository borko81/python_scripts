import multiprocessing
import random


def rand_num(queue):
    num = random.random()
    queue.put(num)


if __name__ == '__main__':
    quequ = multiprocessing.Queue()

    process = [multiprocessing.Process(target=rand_num, args=(quequ,)) for _ in range(4)]

    for p in process:
        p.start()

    for p in process:
        p.join()

    result = [quequ.get() for p in process]
    print(result)