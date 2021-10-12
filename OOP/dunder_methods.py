from functools import total_ordering


class Room:
    def __init__(self, name: str, lenght: float, width: float) -> None:
        self.name = name
        self.lenght = lenght
        self.width = width
        self.square = self.lenght * self.width


class House:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms = list()

    @property
    def living_space(self):
        return sum(r.square for r in self.rooms)

    def add_room(self, room):
        self.rooms.append(room)

    def __str__(self):
        return f"{self.name}: {self.living_space} with style {self.style}"

    def __eq__(self, other):
        return self.living_space == other.living_space


h1 = House('h1', 'House 1')
h1.add_room(Room('Bedroom', 14, 10))
h1.add_room(Room('Kitchen', 10, 10))
print(h1)
