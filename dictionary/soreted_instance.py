from operator import attrgetter

class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f"Name is {self.name} and age is {self.age}"
    
    
l = [User("Name One", 10), User("Name Two", 12), User("Name Three", 5)]


print(sorted(l, key=lambda x: -x.age))
print(sorted(l, key=attrgetter('age')))