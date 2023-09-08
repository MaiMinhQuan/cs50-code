import re



name = input("Name: ")
match = re.search(r"^(?:\w|' ')+", name)
print(match)