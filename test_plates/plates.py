def main():
    s = input("Plate: ")
    if is_valid(s):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s)<2 or len(s)>6 return False
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    for i in range(len(s)):
        if s[0].isdigit()
