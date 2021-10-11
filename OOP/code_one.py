import math


def odd(number: int) -> bool:
    return number & 1 == 1


class Point:

    def move(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def reset(self) -> None:
        self.move(0, 0)

    def calculate(self, other: 'Point') -> float:
        return math.hypot(self.a - other.a, self.b - other.b)


p1 = Point()
p1.move(11, 23)
p2 = Point()
p2.move(10, 10)
print(p1.calculate(p2))
