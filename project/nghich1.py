import re

name = input("Name: ")
if re.search(r"^[a-z]+$", name):
    print("Valid")
else:
    print("Invalid")
