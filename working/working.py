import sys
import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    match = re.search(r"^([0-9][0-2]?):?([0-5][0-9])? ([AP]M) to ([0-9][0-2]?):?([0-5][0-9])? ([AP]M)$", s)
    if match:
        a = match.groups()
        if int(a[0]) > 12 or int(a[3]) > 12:
            raise ValueError
        if int(a[1]) >= 60 or int(a[4]) >= 60:
            raise ValueError
        return a

    else:
        raise ValueError

if __name__ == "__main__":
    main()