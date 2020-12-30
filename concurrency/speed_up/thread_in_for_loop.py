import threading
import time
import random


def execute_thread(i):
    """Take one parameter sleep and return message for complete task"""
    print(f"Start execute thread {i}")
    time.sleep(random.randint(2, 4))
    print(f"Thread {threading.current_thread().name} finished")


for i in range(1, 5):
    th = threading.Thread(target=execute_thread, args=(i, ), name=i)
    th.start()
    th.join()

print(threading.enumerate())
