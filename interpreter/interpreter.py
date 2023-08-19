s = input("Expression: ")
result = str(round(eval(s),1))
print(result, end="")
if "." not in result:
    print(".0")
