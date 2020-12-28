import threading


class myWorkerThread(threading.Thread):
    def __init__(self):
        print("Hello from thread")
        threading.Thread.__init__(self)

    def run(self):
        print("Thread is now run\n")


print("Create thread object")
my = myWorkerThread()
my.start()
print("Thread started")
my.join()
