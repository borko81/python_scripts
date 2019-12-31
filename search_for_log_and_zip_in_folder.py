"""Search for files in directory, without using os.walk module
finally after found file, zip (maybe delete from original posiiton)"""

# Module import
import os
import zipfile
import datetime
import logging

# Hard code param
# Thiks is folder where looked for file or logger
FOLDER_LOOKED = r"C:\Users\borko\Desktop\network_arisa"

# Get curent date to append in zip folder
date = datetime.datetime.now()
folder_with_date = date.strftime("%d-%m-%Y")

# Folder where contains zipped folder and log file
FOLDER_CONTAINS_ZIPPED = r"C:\Users\borko\Desktop"
FOLDER_CONTAINS_ZIPPED_WITH_TIMESTAMP = os.path.join(
    FOLDER_CONTAINS_ZIPPED, folder_with_date)

# logging configuretions
logger_format = '%(asctime)s - %(message)s'
logging.basicConfig(filename=os.path.join(FOLDER_CONTAINS_ZIPPED, 'result.log'),
                    level=logging.INFO, format=logger_format,
                    datefmt="%d.%m.%Y %H:%M")


# Function and classes begin
def zip_file(result_checker):
    """Function open zip folder and put in files include in found_result
    """
    with zipfile.ZipFile(FOLDER_CONTAINS_ZIPPED_WITH_TIMESTAMP + ".zip", mode='a') as z:
        for line in result_checker:
            z.write(line)
    logging.info("All done")


class ZipMe:
    """Enter recursively in folder
    """

    def __init__(self, FOLDER_LOOKED):
        self._path = FOLDER_LOOKED
        self.list_with_result = []

    def search_for_files(self, folder):
        # Check position is file or folder if is folder,
        # enter in and recusr function...
        # Finally return list with found path to filenam's
        if folder is None:
            folder = self._path
        else:
            folder = folder
        os.chdir(folder)
        for f in os.listdir(folder):
            name = os.path.join(folder, f)
            if os.path.isfile(name):
                self.list_with_result.append(name)
            if os.path.isdir(name):
                self.search_for_files(folder=name)
        return self.list_with_result

    def __repr__(self):
        return f"Try to check file's in folder {self._path}"


if __name__ == '__main__':
    test = ZipMe(FOLDER_LOOKED).search_for_files(FOLDER_LOOKED)
    zip_file(test)
