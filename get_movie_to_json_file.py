# LOOKED IN FOLDER, GENERATE JSON WITH NAME AMD FILENAMES
# WRITE DATA IN JSON FILE AND MAY LOAD DATA FROM THIS FILE
# FILENAME NOT CONTAINS OS.PATH.JOIN!

# IMPORT MODULE'S
import json
import os
from collections import defaultdict
from pprint import pprint
import json

# HARCODE PARAM IF WHANT
FOLDER = r'D:\movies'

class Found:
    """
    Generate class with require param's
    """
    def __init__(self, path, files):
        self.path = path
        self.files = files

    def json(self):
        """Result in human readable format"""
        return {
            "path": self.path,
            "files": self.files
        }    


class SearchInFolder:
    """
    Main class, generate, result
    """
    RESULT = []

    def __init__(self, crit, FOLDER=FOLDER):
        self.FOLDER = FOLDER
        self.crit = crit

    def __repr__(self):
        return self.FOLDER

    def search_by_criteria(self):
        foundet = defaultdict(list)
        for root, _, filename in os.walk(self.FOLDER):
            for file in filename:
                if file.endswith(self.crit):
                    foundet[root].append(file)

        return foundet

    def to_json_format(self):
        for k, v in self.search_by_criteria().items():
            SearchInFolder.RESULT.append(Found(v, k).json())
        return SearchInFolder.RESULT

    def write_in_files(self):
        with open(f'{self.crit}.json', 'w') as f:
            json.dump(self.to_json_format(), f)

    @classmethod
    def get_from_file(cls, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                data = json.load(f)
                for p in data:
                    SearchInFolder.RESULT.append(Found(p['path'], p['files']).json())
            return SearchInFolder.RESULT
        else:
            print("Error path not exists")


if __name__ == '__main__':
    # RETURN DATA FROM FILE
    # print(SearchInFolder.get_from_file('avi.json')[0]['files'])

    # WRITE DATA IN FILE
    # SearchInFolder('avi').write_in_files()