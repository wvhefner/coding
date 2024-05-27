import random

print("Enter your password:")
passwd = input()
user_pwd = 0.8614645376384439
random.seed(passwd)

if random.random() == user_pwd:
    print("Password success")

else:
    print("Incorrect Password")
