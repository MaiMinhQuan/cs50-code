import sys
import csv

def main():
    check_input()
    


def check_input():
    if len(sys.argv) < 3:
        sys.exit("Too few  command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

if __name__ == "__main__":
    main()