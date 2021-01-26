import os
FILE = 'my_first_file.txt'

if not os.path.exists(FILE):
    file = open(FILE, 'w')
    # with this should to concat str with \n for next line
    file.write('I just created my first file!' + '\n')
    # with this not add \n to the end for next row
    print("This is another varian to write in file", file=file)
    file.write('I just created my first file!' + '\n')
    # close file
    file.close()
else:
    print("File {} found terminated execution".format(FILE))
