import shelve


class Record:

    def __init__(self, name, age):
        self.name = name
        self.age = age


r1 = Record('First', 10)
r2 = Record('Second', 20)


# To write in shelve
def to_write():
    shelf = shelve.open('db')
    shelf['one'] = r1
    shelf['two'] = r2

    print(shelf)

# To read from shelve
def read_shelfe():
    shelf = shelve.open('db')
    print(shelf['two'].name)
    print(shelf.items())


read_shelfe()