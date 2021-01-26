import os
FILE = 'my_first_file.txt'


if not os.path.exists(FILE):
    print("File already deleted!")
else:
    os.remove(FILE)
