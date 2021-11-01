from dataclasses import dataclass
from abc import ABC, abstractmethod
from enum import Enum, auto


class Parameter(Enum):
    JSON = auto()
    CSV = auto()


class Base(ABC):
    @abstractmethod
    def show_data(self):
        pass


@dataclass
class JsonRepresent(Base):
    data: str

    def show_data(self):
        return {'data': self.data}


@dataclass
class CsvRepresent(Base):
    data: str

    def show_data(self):
        return f"Data;{self.data}"


global_param = {
    'JSON': lambda x: JsonRepresent(x),
    "CSV": lambda x: CsvRepresent(x)
}


class Result:
    def __new__(cls, param, *args, **kwargs):
        return global_param[param](*args, **kwargs)


if __name__ == '__main__':
    result = Result(Parameter.CSV.name, "Some data")
    print(result.show_data())
