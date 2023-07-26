is_the_best = True
print(type(is_the_best))

username = "Bob"

valid_user = username or "User"
print("Hello", valid_user)

username1 = "Bob"
username2 = "Alice"

valid_user1 = username1 and username2
print("hello", valid_user1)