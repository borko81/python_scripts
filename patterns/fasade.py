class Washing:
    def wash(self):
        print("Washing...")


class Rinsing:
    def rinse(self):
        print("Rinsing...")


class Spinning:
    def spin(self):
        print("spinning...")


class WashingMachine:

    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spining = Spinning()

    def startWashing(self):
        self.washing.wash()
        self.rinsing.rinse()
        self.spining.spin()


if __name__ == "__main__":

    washingMachine = WashingMachine()
    washingMachine.startWashing()
