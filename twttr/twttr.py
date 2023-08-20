s = input("Input: ")
print("Output: ", end = "")
for i in s:
    if i not in ["u", "e", "o", "a", "i", "U", "E", "O", "A", "I"]:
        print(i, end = "")
print()