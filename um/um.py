import re

def main():
    print(count(input("Input: ")))

def count(s):
    a = re.findall(r"\b\W*um\W*", s, re.IGNORECASE)
    return len(a)

if __name__ == "__main__":
    main()