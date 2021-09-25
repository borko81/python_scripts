import json

data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]

data_string = json.dumps(data, indent=4)

print(data_string)