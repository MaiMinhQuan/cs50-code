a = {}

while True:
    try:
        s = input()
    except EOFError:
        print()
        break
    s = s.upper()
    if s in a:
        a[s]+=1
    else:
        a[s] = 1

