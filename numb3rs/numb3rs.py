import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        


if __name__ == "__main__":
    main()

