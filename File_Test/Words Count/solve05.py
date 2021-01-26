import os
import re
from typing import List


FILE_TO_READ = 'words.txt'
FILE_TO_CHECK = 'text.txt'


def get_searched_word(file: str) -> List[str]:
    ''' Return list with word who search '''
    result = []
    with open(file, 'r') as f:
        for line in f.readlines():
            result.extend(line.split())
    return result


def search_word_in_file(file: str) -> List[str]:
    all_word = []
    with open(file, 'r') as f:
        for line in f.readlines():
            all_word.extend([word.lower() for word in re.split('\s|,|\.', line[1:])])
    return all_word


def write_result_to_file(file, found) -> None:
    with open(file, 'w') as f:
        for key, value in found:
            print(f'{key} - {value}', file=f)


if __name__ == '__main__':
    # get list with searched words
    searched_words = get_searched_word(FILE_TO_READ)

    # get list with all words in file which read
    text_file_to_read = search_word_in_file(FILE_TO_CHECK)

    # generate dict with all acquirency
    calculate_sum_word = {word: text_file_to_read.count(word) for word in searched_words}

    # soreted dict
    found_word_in_file = sorted(calculate_sum_word.items(), key=lambda x: -x[1])

    # write data to out file
    write_result_to_file('result.txt', found_word_in_file)
