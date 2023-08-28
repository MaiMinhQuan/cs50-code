import sys
import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    match = re.search(r"^([0-9][0-2]?:?([0-5][0-9])?) ([AP]M) to ([0-9][0-2]?:?([0-5][0-9])?) ([AP]M)$", s)
    if match:
        a = match.groups()
        return a
    else:
        raise ValueError

if __name__ == "__main__":
    main()