s = input("What time is it? ")
x,y = s.split(":")
x = float(x)
y = float(y)

if x==7 and (0<=y<=59):
    print("")