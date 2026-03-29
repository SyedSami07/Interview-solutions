
#dsa: Find Top Active User

users = [
    {"name": "sami", "posts": 5},
    {"name": "suhan", "posts": 12},
    {"name": "syed", "posts": 8}
]

top_user = users[0]

for user in users:
    if user["posts"] > top_user["posts"]:
        top_user = user

print(top_user["name"])