while True:
    try:
        n = float(input("Change owed: "))
        if n < 0:
            continue
        break
    except:
        continue

n = int(n * 100)
quarter = int(n / 25)
n %= 25
dime = int(n / 10)
n %= 10
nickel = int(n / 5)
n %= 5

print(quarter + dime + nickel + n)
