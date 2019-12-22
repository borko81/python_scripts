# __Borko__

# Import some modules
# Clear cmd
import os
# Time sleep, use unifotm to get more advance time sleep
import time
# Threading
import threading
# To use uniform, needed to time module
import random


# Phrace
word = """Merry
Cristmass
Bitchess"""

# Hard code param is next some line's
LEGEND = {'e': 'red', 's': 'blue', 'm': 'yellow'}

red = []
blue = []
yellow = []

for position, char in enumerate(word):
    if LEGEND.get(char.lower()) == 'red':
        red.append(position)
    if LEGEND.get(char.lower()) == 'blue':
        blue.append(position)
    if LEGEND.get(char.lower()) == 'yellow':
        yellow.append(position)


def customize(color):
    """ 
        Use Lock, if not two or more thread clear screen! (TOTAL)

    """
    SEM = threading.Lock()

    if color == 'origin':
        SEM.acquire()
        time.sleep(random.uniform(1, 3))
        os.system('cls')
        SEM.release()
        for pos, char in enumerate(word):
            if pos in red:
                print(f'\033[91m{char}\033[0m', end='')
                continue
            if pos in blue:
                print(f'\033[94m{char}\033[0m', end='')
                continue
            if pos in yellow:
                print(f'\033[93m{char}\033[0m', end='')
                continue
            else:
                print(char, end='')
                continue
        print()
    if color == 'back':
        SEM.acquire()
        time.sleep(random.uniform(1, 3))
        os.system('cls')
        SEM.release()
        for pos, char in enumerate(word):
            if pos in red:
                print(f'\033[93m{char}\033[0m', end='')
                continue
            if pos in blue:
                print(f'\033[94m{char}\033[0m', end='')
                continue
            if pos in yellow:
                print(f'\033[91m{char}\033[0m', end='')
                continue
            else:
                print(char, end='')
                continue
        print()


def insane():
    # Thread's in this funcion
    # without join system is blow :)
    colored_one = threading.Thread(target=customize, args=('origin',))
    colored_two = threading.Thread(target=customize, args=('back',))
    colored_one.start()
    colored_two.start()
    colored_one.join()
    colored_two.join()


if __name__ == '__main__':
    os.system('color')
    while 1:
        insane()
