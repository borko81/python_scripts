class ShowInfo:

    def __repr__(self):
        return f"{self.name} is {self.age} years old"


class Person(ShowInfo):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


class AllPerson(Person):
    persons = []

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        AllPerson.persons.append(self)

    @classmethod
    def find_by_name(cls, name):
        return [p for p in AllPerson.persons if p.name == name][0]


p1 = AllPerson("One", 10)
p2 = AllPerson("Two", 20)
p3 = AllPerson("Three", 30)


print(AllPerson.find_by_name('Two'))