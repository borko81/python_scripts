def check_param(x):
    if not isinstance(x, (int, float)):
        raise ValueError(f"{x} is not allowed")


class MyError(Exception):
    pass


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = check_param(x) or x
        self.y = check_param(y) or y

    def __repr__(self) -> str:
        return f"{self.x} _ {self.y}"

    def __new__(cls, *args, **kwargs):
        print(f"Create new isntance")
        return super().__new__(cls)


class Person:
    def __init__(self, name: str) -> None:
        self.name = name


class Employee(Person):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            return cls._instance
        raise MyError("Only one instance allowed")

    def __init__(self, name, town=False):
        super().__init__(name)
        self.town = town

    @property
    def show_town(self):
        if not self.town:
            return "Error"
        return "The town is {}".format(self.town)


e = Employee("Name", "Vel")
b = Employee("Name2", "Vel2")
print(e.show_town)
