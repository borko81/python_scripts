import time
import logging


# for i in range(1, 10):
#     print(f"{i} - {time.perf_counter()}")
    
    
class TimerError(Exception):
    """ Custom timer exception """

    
class Timer:
    def __init__(self, logger):
        self.__start_time = None
        self.logger = logger
        
    def start(self):
        if self.__start_time is not None:
            raise TimerError(f"Timer is running")
        
        self.__start_time = time.perf_counter()
        
    def stop(self):
        if self.__start_time is None:
            raise TimerError("Timer is not running")
        
        elapsed_time = time.perf_counter() - self.__start_time
        self.__start_time = None
        self.logger(elapsed_time)
        
        
t = Timer(logger=logging.warning)
t.start()        
        
for i in range(1, 10):
    print(i, end=' ')
    
print("\n")
t.stop()