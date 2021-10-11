FILE_NAME = 'text.txt'

with open(FILE_NAME) as f:
    while True:
        try:
            line = next(f)
            print(line, end='')
        except StopIteration:
            break
