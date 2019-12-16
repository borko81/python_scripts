"""
Search for file wit empty space in name, if found,
add this file to log file. Read This file and rename
with replace empty spalce with '_'
"""

# Import modules
import os

# Some hardcode param
Path = r'C:\Users\borko\Desktop\trii'
search_patter = ' '
log_file = 'changes.log'


class Main:

    def __init__(self, path, search_patter):
        assert os.path.exists(path)
        self._path = path
        self._search = search_patter

    def search_for_files(self):
        result = []
        for root, dirname, filename in os.walk(self._path):
            for file in filename:
                if self._search in file:
                    result.append(os.path.join(root, file))
        return result

    def write_to_log_file(self):
        with open(log_file, 'w') as f:
            for line in self.search_for_files():
                f.write(line + "\n")

    def change_filename(self):
        self.write_to_log_file()

        for file in open(log_file, 'r'):
            file = file.rstrip('\n')
            new_file = os.path.basename(file).replace(' ', '_')
            new_directory = os.path.dirname(file)
            rename_file = new_directory + "\\" + new_file
            os.rename(file, rename_file)


if __name__ == '__main__':
    test = Main(Path, search_patter)
    test.change_filename()
