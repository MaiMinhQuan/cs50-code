t = 50
while t>0:
    print(f"Amount Due: {t}")
    c = int(input("Insert Coin: "))
    if c in [5, 10, 25]:
        t-=c
if t<0:
    t=-t
print(f"Change Owed: {t}")