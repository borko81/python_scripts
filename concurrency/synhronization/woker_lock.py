import threading
import time
import random
counter = 0
lock = threading.Lock()


def worker_a():
    global counter
    lock.acquire()
    try:
        while counter < 10:
            counter += 1
            print('Worker A increment counter to {}'.format(counter))
            time.sleep(random.randint(0, 1))
    finally:
        lock.release()


def worker_b():
    global counter
    lock.acquire()
    try:
        while counter > -5:
            counter -= 1
            print('Worker B increment counter to {}'.format(counter))
            time.sleep(random.randint(0, 1))
    finally:
        lock.release()


def main():
    thread_one = threading.Thread(target=worker_a)
    thread_two = threading.Thread(target=worker_b)
    thread_one.start()
    thread_two.start()
    thread_one.join()
    thread_two.join()


if __name__ == '__main__':
    main()
