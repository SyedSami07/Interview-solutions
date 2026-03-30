
#  Login System — Check Username Fast

users = ["sami", "rahim", "karim", "tamim", "rafi"]
user_set = set(users)

login_user = "karim"

if login_user in user_set:
    print("Login Success")
else:
    print("User Not Found")