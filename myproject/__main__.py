from name import User, ListWithUsers

u1 = User('borko')
u2 = User('george')
users = ListWithUsers()
users.add_user(u1)
users.add_user(u2)
users.remove_user('borko')
print(users.show_users())