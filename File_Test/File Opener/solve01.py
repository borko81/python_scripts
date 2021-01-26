import os
FILE_NAME = 'text.txt'


def check_for_file(file):
    try:
        f = open(file, 'r')
    except IOError:
        print("File not found")
    else:
        print("File found")


check_for_file(FILE_NAME)
