import sys

def main():
    check_input()
    try:
        with open(sys.argv[1]) as file:
            a = file.readlines()
    except:
        sys.exit("File does not exist")

    cnt = 0
    for line in a:
        if check_line(line) == False:
            cnt+=1

    print(cnt)


def check_input():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) >2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")c

def check_line(line):
    if line.isspace() == True:
        return True
    if line.lstrip().startswith("#") == True:
        return True
    return False

if __name__ == "__main__":
    main()
