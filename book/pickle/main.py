import pickle
import pprint
from typing import Dict

data = [{'a': 'A', 'b': 2, 'c': 3.0}]

# return data to binary format
data_string = pickle.dumps(data)
pprint.pprint(data_string)

# return from binary to data foramt
print(pickle.loads(data_string))


class TwoInOne:
    def __init__(self, name: str) -> str:
        self.name = name
        self.rev_name = name[::-1]

    @property
    def show_data(self) -> Dict:
        return {'name': self.name, 'rev_name': self.rev_name}

    @staticmethod
    def doc() ->str:
        return "Return name and reversed name"

    def __str__(self) -> str:
        return f"{self.name}: {self.rev_name}"


test_one = TwoInOne('Some name')
test_one_pickle_data = pickle.dumps(test_one)
print(test_one_pickle_data)

returned_data_one = pickle.loads(test_one_pickle_data)
print(returned_data_one.show_data)
print(returned_data_one.doc())