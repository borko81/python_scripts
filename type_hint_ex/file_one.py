from typing import Union, List


allowed_number = Union[int, float]


def add_old(x: allowed_number, y: Union[int, float]) -> Union[int, float]:
    return x + y


# Python 3.10


def add(x: int | float, y: int | float) -> int | float:
    return x + y


print(add(10, 0.1))


def show_something() -> None:
    numbers: List[allowed_number] = [1, 2, 4.2]
    print(numbers)
    

show_something()