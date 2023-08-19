s = input("Expression: ")
result = round(eval(s),1)
if (result==eval(s)):
    print(f"{result}.0")
else:
    print(result)