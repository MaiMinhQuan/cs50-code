import re

def main():
    print(count(input("Input: ")))

def count(s):
    s=
    a = re.findall(r"\b\W*um\W*", s)
    return len(a)

if __name__ == "__main__":
    main()