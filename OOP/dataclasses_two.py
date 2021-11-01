from dataclasses import dataclass, field
from typing import ClassVar

@dataclass(order=True, frozen=True)
class Person:
    price: ClassVar = 100
    sort_index: int = field(init=False, repr=False)
    name: str
    age: int
    strength: int = field(default=100)

    def __post_init__(self):
        object.__setattr__(self, 'sort_index', self.strength)


person_one = Person("Bob", 40)
person_two = Person("Alice", 45, strength=150)
print(person_one)
print(person_one.price)

print(person_one == person_two)
print(person_one < person_two)