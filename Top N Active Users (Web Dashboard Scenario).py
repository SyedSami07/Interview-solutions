users = [
    {"name": "sami", "posts": 5},
    {"name": "rahim", "posts": 12},
    {"name": "karim", "posts": 8},
    {"name": "tamim", "posts": 15},
    {"name": "rafi", "posts": 3}
]
N = 3

# sort descending by 'posts'
users_sorted = sorted(users, key=lambda x: x["posts"], reverse=True)

# extract top N names
top_users = [user["name"] for user in users_sorted[:N]]

print(top_users)