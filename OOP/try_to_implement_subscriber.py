class Person:
    def __init__(self, name) -> None:
        self.name = name

    def update(self, message, channel):
        print(f"Hello {self.name} this is a new message: {message} in channel {channel}")


class Channel:
    def __init__(self, name) -> None:
        self.name = name
        self.__subscriber = []
        self.article = []

    def add_new_subscriber(self, person: Person):
        self.__subscriber.append(person)
        print(f"{person.name} was added successfully")

    def remove_subscriber_from_list(self, person: Person):
        self.__subscriber.remove(person)
        print(f"{person.name} was remove successfully")

    def notify_user(self, article):
        for person in self.__subscriber:
            person.update(article, self.name)

    def show_articles(self):
        [print(name) for name in self.article]


class Article:
    def __init__(self, chanel: Channel) -> None:
        self.chanel = chanel

    def add_new_article(self, article):
        self.chanel.article.append(article)
        self.chanel.notify_user(article)


if __name__ == "__main__":
    p = Person("Test User")
    channel = Channel("This is a new book")
    channel.add_new_subscriber(p)
    a1 = Article(channel)
    a1.add_new_article("AR 1")
    a2 = Article(channel)
    a2.add_new_article("AR 2")
