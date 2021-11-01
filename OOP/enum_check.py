from abc import ABC, abstractmethod
import enum
from dataclasses import dataclass, field


class AnimalsName(enum.Enum):
    dog = enum.auto()
    cat = enum.auto()
    lion = enum.auto()


@dataclass
class Animal:
    animal: str


a = Animal(AnimalsName.cat)
# print(a.animal.value)


class Base(ABC):
    @abstractmethod
    def show_message(self):
        pass


class Season(enum.Enum):
    SPRING = enum.auto()
    AUTUMN = enum.auto()


print(list(Season))


class Spring(Base):
    @staticmethod
    def show_message():
        return "I love Spring"


class Autumn(Base):
    @staticmethod
    def show_message():
        return "I love Autumn"


answer = {"SPRING": Spring.show_message, "AUTUMN": Autumn.show_message}


choice = Season.SPRING.name
print(answer[choice]())
