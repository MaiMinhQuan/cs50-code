import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

"""def validate(ip):
    try:
        if matches := re.search("^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
            a = int(matches.group(1))
            b = int(matches.group(2))
            c = int(matches.group(3))
            d = int(matches.group(4))
            if


