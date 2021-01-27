import string


def calc_letters(line) -> int:
    return sum(
        [
            len([letter for letter in x if letter.isalpha()])
            for x in line.split()
        ]
    )


def calc_punctuatuon(line) -> int:
    return len([x for x in line if x in string.punctuation])


def read_file(filename, output_file):
    with open(filename, 'r') as f:
        with open(output_file, 'w') as file_to_write:
            for pos, line in enumerate(f.readlines(), start=1):
                letter_count = calc_letters(line)
                punctuation_count = calc_punctuatuon(line)
                print(f'Line {pos}: {line} ({letter_count}) ({punctuation_count})', file=file_to_write)


if __name__ == '__main__':
    read_file('file_for_test.txt', 'output_file.txt')
