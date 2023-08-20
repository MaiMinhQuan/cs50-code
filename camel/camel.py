s = input("camelCase: ")

for i in s:
    if i.isupper()==True:
        print(f"_{i.tolower()}", end = "")
    else:
        print(i, end = "")