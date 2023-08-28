import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        if matches := re.search(r"(http(s)*:\/\/(www\.)*youtube\.com/embed\/)([a-z_A-Z_0-9]+)", s):
            url = matches.group
            return "https://youtu.be/" + url[3]

if __name__ == "__main__":
    main():