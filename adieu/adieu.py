import inflect

p = inflect.engine()
a = []
while True:
    try:
        s = input("Name: ")
        a.append(s)
    except EOFError:
        print()
        break

print(f"Adieu, adieu, to {p.join(a)}")