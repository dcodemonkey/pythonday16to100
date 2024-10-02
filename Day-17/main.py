class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1




user_1 = User(140, "Kunal")
user_2 = User(150, "Supriye")
# print(user_2.followers)


user_1.follow(user_2)
user_2.follow(user_1)
print("User_1 follower: " ,user_1.followers)
print("User_1 following",user_1.following)
print("User_2 follower: " ,user_2.followers)
print("User_2 following",user_2.following)


