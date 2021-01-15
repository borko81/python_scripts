# Impot module, sys for get argv, getpass for secure enter pw
import sys
from getpass import getpass


def check_name():
    '''
        Check name is enter from line, if not ask user to enter username, then password
    '''
    try:
        name = sys.argv[1]
    except IndexError:
        name = input("What is your name: ")
    else:
        print(name)

    pw = getpass("Enter password")
    print(f"{name} - {pw}")


if __name__ == '__main__':
    check_name()
