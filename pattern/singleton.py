class Singleton_Genius(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if not Singleton_Genius.instance:
            Singleton_Genius.instance = object.__new__(cls)
        return Singleton_Genius.instance

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


if __name__ == "__main__":
    s1 = Singleton_Genius("Yang", "Zhou")
    s2 = Singleton_Genius("Elon", "Musk")
    print(s1.first_name)
