import sys
import csv

def main():
    check_input()
    after = []
    try:
        with open(sys.argv[1]) as before:
            reader = csv.DictReader(before)
            for row in reader:
                last


def check_input():
    if len(sys.argv) < 3:
        sys.exit("Too few  command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

if __name__ == "__main__":
    main()