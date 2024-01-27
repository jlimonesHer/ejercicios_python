class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0

user_one = User("001", "Limones")
print(user_one.name)