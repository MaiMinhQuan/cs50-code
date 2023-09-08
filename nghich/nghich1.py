import re

name = input("Name: ")
if re.search(r"^\w+", name):
    print("Valid")
else:
    print("Invalid")
