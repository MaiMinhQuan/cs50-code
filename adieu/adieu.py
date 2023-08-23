import inflect

p = inflect.engine()
a = []
while True:
    try:
        s = input("Name: ")
        a.append(s)
    except EOFError:
        break