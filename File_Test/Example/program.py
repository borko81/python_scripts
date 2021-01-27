# Import module
import os

# Hard code file, extend to Desktop
OUT_FILE = 'report.txt'
FILE_WITH_RESULT = os.path.join(os.environ['USERPROFILE'], 'Desktop', OUT_FILE)

# Here add extension from found file with, theirs name's
name_of_files = {}


def write_output_to_file(outfile, data_to_write):
    """ Function use to write result in needed file"""
    with open(outfile, 'w') as f:
        print(data_to_write, file=f)


def show_output(dirst_with_files):
    """ Function used to generate output result """
    result = ''
    for key, value in sorted(dirst_with_files.items()):
        result += key + '\n'
        for v in value:
            result += f'- - - {v}{key}\n'
    return result


def traverse_directory(directory, dirst_with_files):
    """ Function used to traverse directory and  sumarized result """
    files = os.listdir()
    for file in files:
        name, extension = os.path.splitext(file)

        if extension not in dirst_with_files:
            dirst_with_files[extension] = []
        dirst_with_files[extension].append(name)
    show_output(dirst_with_files)


if __name__ == '__main__':
    traverse_directory(os.getcwd(), name_of_files)
    write_output_to_file(FILE_WITH_RESULT, show_output(name_of_files))
