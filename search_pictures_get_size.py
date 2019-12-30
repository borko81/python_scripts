# __borko__

"""Get picutes from folder, search them by format.
Use module cv2 to reshape img and get his width, hight and channel
show result in terminal
Script is good to moove some item in folder by use criteria"""

import os
import sys
import cv2
import multiprocessing
FOLDER = r'C:\Users\borko\Pictures'


class Insane:

    def __init__(self, folder):
        self._search_for_this = ["jpg", "png"]
        try:
            os.path.exists(folder)
        except OSError as e:
            print(e)
            sys.exit()
        else:
            self._path = folder

    def search_pictures(self):
        # use listdir to get pictures from folder, do not lookup in recursive folder
        result = [os.path.join(self._path, i) for i in os.listdir(self._path) if i.split(
            ".")[-1] in self._search_for_this]
        return result

    def use_csv_to_size(self, pic):
        # use cv2 to get height, and width from item
        img = cv2.imread(pic)
        height, width, channel = img.shape
        return (pic, height, width, channel)

    def magic(self, pic):
        # calculate size and return result
        # use os.syste to delete, remove or whatever wants
        pic, height, width, channel = self.use_csv_to_size(pic)
        if (width >= 1920 and height >= 1080):
            print(f"{pic} has 1080px")
            return pic
        elif (width >= 1280 and height >= 720):
            print(f"{pic} has 720px")
            return pic
        else:
            print(f"{pic} has some unsuported format")
            return pic

    def calculate_size(self):
        # FINAL MODUL
        # UNCOMENT UNDER IF PICTURE'S NOT TOO MANY

        # for im in self.search_pictures():
        #     self.magic(im)

        # USE UNDER ONLY IF PICTURES IS TOO MANY
        # IF NUMBER IS SMALL, POOL IT WILL BE FUN RESULT
        p = multiprocessing.Pool(4)
        r = p.map(self.magic, self.search_pictures())
        list(r)


if __name__ == '__main__':
    test = Insane(FOLDER)
    test.calculate_size()
