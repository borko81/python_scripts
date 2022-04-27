import os

escape_char = '#'
fname = input("Enter path to filename :")
result = []

try:
    os.path.exists(fname) is True
    for line in open(fname):
        if len(line) > 1 and line[0] != escape_char:
            result.append(line.strip())
except:
    print("Filename %s is not correct" % fname)


if len(result) == 0:
    print("Not found result")
else:
    for line in result:
        print(line)
