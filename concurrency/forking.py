import os


def child():
    print("Child process %d" % os.getpid())


def parent():
    print("Parent process %d" % os.getpid())
    newRef = os.getpid()
    if newRef == 0:
        child()
    else:
        print("In parent process %d" % newRef)


parent()