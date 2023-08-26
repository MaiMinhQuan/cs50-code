import sys
import tabulate
import csv

def main():
    check_input()
    pizza = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                pizza.append(row)
    except:
        sys.exit("File does not exit")

    print(pizza)
    #print(tabulate(pizza[1:], headers = pizza[0], tablefmt = "grid"))


def check_input():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()