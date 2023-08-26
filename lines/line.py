import sys

def main():
    check_input()
    try:
        with open()



def check_input():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) >2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

def check_line(line):
    if line.isspace() == True:
        return True
    if line.lstrip().startwith("#") == True:
        return True

if __name__ == "__main__":
    main()
