s = input("Input: ")
print("Output: ", end = "")
for i in s:
    if i not in [u, e, o, a, i]:
        print(i, end = "")
print()