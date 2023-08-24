def main():
    s = input("Plate: ")
    if is_valid(s):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s)<2 or len(s)>6:
        return False
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    for i in range(len(s)-1):
        if s[i].isdigit() == True and s[i+1].isalpha() == True:
            return False
        if s[i].isalpha() == True and s[i+1] == "0":
            return False
    for i in s:
        if i.isalnum() == False:
            return False
    return True

if __name__ == "__main__":
    main()