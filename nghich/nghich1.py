import re
def check_name(name):
    return re.search(r"^(?:\w|' ')+", name)


name = input("Name: ")
print(check_name(name))