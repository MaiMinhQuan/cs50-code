a = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

while True:
    s = input("Date: ")
    try:
        if "/" in s:
            x,y,z = map(int, s.split("/"))
            if y>31 or x>12:
                continue
            break
        elif "," in s:
            s = s.replace(",", "")
            x,y,z = s.split(" ")
            if x in a:
                x = a.index(x)+1
                y = int(y)
                z = int(z)
                if y>31:
                    continue
                break
        else:
            continue
    except ValueError:
        continue
print(f"{z}-{x:02}-{y:02}")
