import re
email = "^[a-z]+[\._]?[a-z 0-9] + [@]\w + [.]\w{2,3}$"
user_email = input("Enter your email : ")
if re.search(email, user_email):
    print("Right email")
else:
    print("Wrong email")