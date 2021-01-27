import os
FILE_NAME = 'file_for_test.txt'


def read_file(file: str):
    ''' Read File '''
    assert os.path.exists(file)

    with open(FILE_NAME, 'r') as f:
        for num, line in enumerate(f.readlines()):
            if not num % 2:
                yield line


def remove_char_from_line(line):
    ''' Remove ilegal char '''
    ilegal_symbol = ["-", ",", ".", "!", "?"]
    for symbol in ilegal_symbol:
        line = line.replace(symbol, '@')
    return line


def reverse_line(line):
    ''' Reverse string, who read from file '''
    return " ".join(line.split()[::-1])


def main():
    for line in read_file(FILE_NAME):
        line_with_remove_char = remove_char_from_line(line)
        print(reverse_line(line_with_remove_char))


if __name__ == '__main__':
    main()
