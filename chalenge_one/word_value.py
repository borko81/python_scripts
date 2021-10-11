from abc import ABC, abstractclassmethod

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q E")]


LETTERS = {
    letter: score
    for score, letters in scrabble_scores
    for letter in letters.split()
}

FILENAME = 'words.txt'


class Initialize(ABC):

    @abstractclassmethod
    def __init__(self, filename):
        self.filename = filename


class ToUpperCase(Initialize):
    def __init__(self, filename):
        self.filename = filename

    def convert_text_to_upper_case(self):
        with open(self.filename) as f:
            data = map(str.upper, f.readlines())
            for line in data:
                print(line.strip())


class FoundStartWithDies(Initialize):
    def __init__(self, filename):
        self.filename = filename

    def found_lines_who_start_with_dies(self):
        with open(self.filename) as f:
            data = filter(lambda str: str.startswith('#'), f.readlines())
            [print(line.strip()) for line in data]


class AllInOne(ToUpperCase, FoundStartWithDies):

    def __init__(self, filename):
        self.filename = filename


if __name__ == '__main__':
    t = AllInOne(FILENAME)
    t.convert_text_to_upper_case()
