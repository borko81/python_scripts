class Student:

    count = 0
    static_param = 'This is static'

    def __init__(self, name):
        self.name = name
        Student.count += 1

    def show_name(self):
        return self.name

    @classmethod
    def upper_name(cls, name):
        return cls(name.upper())

    @staticmethod
    def show_static():
        return Student.static_param


a = Student('borko')

if not hasattr(a, 'age'):
    setattr(a, 'age', 40)

print(a.__class__.__name__)
