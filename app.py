import os

# This is just a sample insecure code
user_input = input("Enter filename: ")
with open(user_input, "r") as f:
    print(f.read())
