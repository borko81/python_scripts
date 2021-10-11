import csv
from collections import namedtuple
from pprint import pprint
import json

FILE = 'sample.csv'
FILE_TO_WRITE = 'sample.csv'
headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
        ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
        ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
        ]


def reader_one():
    result = {'items': []}
    with open(FILE) as f:
        csv_file = csv.DictReader(f, delimiter=';')
        for line in csv_file:
            result['items'].append(line)
    return json.dumps(result)


def reader_two():
    with open(FILE) as f:
        csv_reader = csv.reader(f, delimiter=';')
        headings = next(csv_reader)
        Row = namedtuple('Row', headings)
        for row in csv_reader:
            line = Row(*row)
            print(line.price)


def write_csv_to_file(filename):
    """
    write csv to file
    :param filename:
    :return:
    """
    with open(filename, 'w', newline='') as f:
        csv_writer = csv.writer(f, delimiter=';')
        csv_writer.writerow(headers)
        csv_writer.writerows(rows)


if __name__ == '__main__':
    print(reader_one())
