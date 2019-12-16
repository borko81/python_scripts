import os
import sys
import csv


class SourceInfo:
    """
    Open file and try to return param from this file
    """

    def __init__(self, filename, delimiter=None):
        self._filename = filename
        if delimiter is None:
            self._delimiter = ';'
        else:
            self._delimiter = delimiter

    def split_info(self):
        """
        Return:
            ('192.168.168.1', 'test', 'password')
        """
        with open(self._filename, 'r') as f:
            csv_file = csv.reader(f, delimiter=self._delimiter)
            for line in csv_file:
                ip, username, password = line
                yield ip, username, password


if __name__ == '__main__':
    mytest = SourceInfo('list_with_ip.csv')
    for line in mytest.split_info():
        print(line)
