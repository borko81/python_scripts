class Person_old:
    def __init__(self, first_name: str) -> None:
        self.set_first_name(first_name)

    # Getter
    def get_first_name(self):
        return self._first_name

    # Setter
    def set_first_name(self, value):
        if not isinstance(value, str):
            raise ValueError("A string expected!")
        self._first_name = value


class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('A string expected!')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError('Cannot delete attribute')


class SubPerson(Person):
    @Person.name.getter
    def name(self):
        print("Invoke name")
        return super().name



p = SubPerson('Yerihon')
print(p.name)
