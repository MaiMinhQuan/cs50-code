a = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

while True:
    s = input("Date: ")
    if "/" in s:
        x,y,z = s.split("/")
    elif "," in s:
        s = s.replace(",", "")
        x,y,z = s.split(" ")
        if x in a:
            x = a.index(x)+1
            break
    else:
        continue

print(f"{z,x,y}", sep=" ")
