from dataclasses import dataclass, field
from typing import ClassVar, List


@dataclass(frozen=True)
class DataClassCard:
    count: ClassVar[int] = 10
    suite: str
    rank: str = field(default='Q')

    def show_result(self):
        return self.suite + ' ' + self.rank + ' ' + str(DataClassCard.count)


@dataclass
class Deck:
    cards: List[DataClassCard]

    def show_from_deck(self):
        return [x.show_result() for x in self.cards]


q1 = DataClassCard("Hearts")
q2 = DataClassCard("Pica", "K")
d = Deck([q1, q2])
print(d.show_from_deck())
