from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return "User({})".format(self.user_id)

users = [User(23), User(11), User(22)]

sorted_users = sorted(users, key=attrgetter('user_id'))

print(sorted_users)

min_user = min(users, key = attrgetter('user_id'))

print(min_user)