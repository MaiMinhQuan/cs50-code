while True:
    s = input("Fraction: ")
    x,y = s.split(" ")
    try:
        x=int(x)
        y=int(y)
        if x>y:
            continue
        break
    except (ValueError, ZeroDivisionError):
        continue

r = x/y*100
