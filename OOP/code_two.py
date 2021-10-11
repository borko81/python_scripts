class Point:

    def __init__(self, name: str = 'First', surname: str = 'Last') -> None:
        '''
        :param name: string Show name
        :param surname: string Show last name
        '''
        self.name = name
        self.surname = surname


human = Point(surname='St')
print(human.name, human.surname)
