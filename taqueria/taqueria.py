a = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

sum=0
while True:
    try:
        s = input("Item: ")
        s = s.title()
    except EOFError:
        print()
        break
    if s in a:
        sum+=a[s]
        print(f"Total: ${sum:.2f}")