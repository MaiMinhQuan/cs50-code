try:
    n = float(input("Change owed: "))
    if n < 0:
        continue
    break
except:
    continue

n = int(n * 100)
