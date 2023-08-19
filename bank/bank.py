s = input("Greeting: ")
s = s.lower().strip()
if s[0:5] == "hello":
    print("$0")
elif s[0] == "h":
    print("$20")
else:
    print("$100")