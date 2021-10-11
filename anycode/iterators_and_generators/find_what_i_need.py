import os
import fnmatch

PATH = os.getcwd()
param_for_looked = 'looked this'


def show_path_when_founded(path):
    for path, dirname, filename in os.walk(path):
        result = fnmatch.filter(filename, '*py')
        for r in result:
            yield os.path.join(path, r)


def traverse_file_for_needed_word(file, boundery):
    with open(file) as f:
        try:
            current_line = next(f)
            if boundery in current_line:
                print(f"Found math in file {file}")
        except StopIteration:
            pass


if __name__ == '__main__':
    for line in show_path_when_founded(PATH):
        traverse_file_for_needed_word(line, 'looked this')