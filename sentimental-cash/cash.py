
while True:
    try:
        n = float(input("Change owed: "))
        if n < 0:
            continue
        break
    except:
        continue

n = int(n * 100)
print(n)
quarter = n / 25
print(quarter)
n -= 25 * quarter
dime = n / 10
n -= 10 * dime
nickel = n / 5
n -= 5 * nickel

#print(quarter + dime + nickel + n)

