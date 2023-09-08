import re

name = input("Name: ")
if re.search(r"[a-zA-Z ]+", name):
    print("Valid")
else:
    print("Invalid")
