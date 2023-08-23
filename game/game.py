import random

while True:
    n = input("Level: ")
    if n.isdigit()==False or int(n)<=0:
        continue
    break

n = int(n)
s = random.randint(1, n)
print(s)

while True:
    i = input("Guess: ")
    if i.isdigit()==False:
        continue
    i = int(i)
    if i>s:
        print("Too large!")
    elif i<s:
        print("Too small!")
    else:
        print("Just right!")
        break




