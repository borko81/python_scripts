class User:

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return self.username


class ListWithUsers:

    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        self.users.append(user)

    def remove_user(self, username: str):
        tem_users = self.find_user(username)
        try:
            self.users.remove(tem_users[0])
        except IndexError:
            return "User %s not found" % username


    def find_user(self, username):
        user = [x for x in self.users if x.username == username]
        return user

    def show_users(self):
        result = "\n".join([u.__repr__() for u in self.users])
        return result


if __name__ == '__main__':
    u1 = User('borko')
    u2 = User('george')
    users = ListWithUsers()
    users.add_user(u1)
    users.add_user(u2)
    users.remove_user('borko')
    print(users.show_users())
