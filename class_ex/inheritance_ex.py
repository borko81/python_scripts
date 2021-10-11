class Animal:
    __data = 'test'

    def speak(self):
        print("Animal can speak")

    @staticmethod
    def show_data():
        return Animal.__data


class Dog(Animal):
    def show_something(self):
        print("This is a dog")

    def speak(self):
        super().speak()
        print("From parrent class")


class SmallDog(Dog):
    def eat(self):
        print("Small dog is hungry")


d = SmallDog()
d.speak()
print(d.show_data())
