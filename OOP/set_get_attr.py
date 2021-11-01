class Employee:

    def __init__(self, data):
        super().__setattr__('data', dict())
        self.data = data

    def __getattr__(self, item):
        if item in self.data:
            return self.data[item]
        return 0

    def __setattr__(self, key, value):
        if key in self.data:
            self.data[key] = value
        else:
            super().__setattr__(key, value)


e = Employee({'age': 23, 'name': 'John'})
print(e.__dict__)
print(e.age)
e.salary = 100
print(e.salary)

setattr(e, 'town', 'Velingrad')
print(e.town)