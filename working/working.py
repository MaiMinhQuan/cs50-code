import sys
import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if match := re.search(r"^([0-9][0-2]?):?([0-5][0-9])? ([AP]M) to ([0-9][0-2]?):?([0-5][0-9])? ([AP]M)$", s):
        a = match.groups()
        if int(a[0]) > 12 or int(a[3]) > 12:
            raise ValueError

        return f"{chuan_hoa(a[0], a[1], a[2])} to {chuan_hoa(a[3], a[4], a[5])}"

    else:
        raise ValueError

def chuan_hoa(g, p, sc):
    if sc == "PM":
        if int(g) == 12:
            g = 12
        else:
            g = int(g) + 12
    else:
        if int(g) == 12:
            g = 0
        else:
            g = int(g)

    if p == None:
        p = "00"

    return f"{g:02}:{p}"

if __name__ == "__main__":
    main()