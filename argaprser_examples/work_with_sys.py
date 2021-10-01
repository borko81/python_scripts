import os
import sys

if len(sys.argv) > 2:
    print("Too many parameter")
    sys.exit()

if len(sys.argv) < 2:
    print("Enter path")
    sys.exit()

PATH = sys.argv[1]

if not os.path.isdir(PATH):
    print("This is not valid")
    sys.exit()

[print(x) for x in os.listdir(PATH)]
