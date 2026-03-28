
#dsa: duplicate username remove

usernames = ["sami", "syed", "sami", "salman", "suhan"]

unique_users = []

for user in usernames:
    if user not in unique_users:
        unique_users.append(user)

print(unique_users)