from abc import ABC, abstractclassmethod
import json

data = [
    {"name": "First", "age": 10},
    {"name": "Second", "age": 20},
    {"name": "LAst", "age": 30},
]


class StrategyBase(ABC):
    @abstractclassmethod
    def convert(data):
        pass


class ConvertToJson(StrategyBase):
    def convert(self, data):
        return json.dumps(data)


class ConvertToCSV(StrategyBase):
    def convert(self, data):
        result = ''
        for line in data:
            result += f"{line['name']};{line['age']}"
        return result


class Convert:
    strategy: StrategyBase

    def __init__(self, strategy: StrategyBase = None) -> None:
        if strategy is None:
            Convert.strategy = ConvertToJson()
        else:
            Convert.strategy = ConvertToCSV()

    def conv(self, data):
        return Convert.strategy.convert(data)


if __name__ == '__main__':
    m = Convert(ConvertToCSV())
    data = m.conv(data)
    print(data)
