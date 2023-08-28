import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if matches := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        a = int(matches.group(1))
        b = int(matches.group(2))
        c = int(matches.group(3))
        d = int(matches.group(4))
        if a < 0 or a > 255:
            return False
        if b < 0 or b > 255:
            return False
        if c < 0 or c > 255:
            return False
        if d < 0 or d > 255:
            return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()

