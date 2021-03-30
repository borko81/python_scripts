from _thread import start_new_thread
from time import sleep

threadId = 1
waiting = 2


def factoriel(n):
    global threadId
    rc = 0

    if n < 1:
        print("{}: {}".format("\nThread", threadId))
        threadId += 1
        rc = 1
    else:
        returnNumber = n * factoriel(n-1)
        print("{}: {}".format(str(n), str(returnNumber)))
        rc = returnNumber
    return rc


start_new_thread(factoriel, (5,))
start_new_thread(factoriel, (4, ))

print("Waiting for threads to return...")
sleep(waiting)