import re

def main():
    print(count(input("Input: ")))

def count():
    a = re.findall(r"\b\W")