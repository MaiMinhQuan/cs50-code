import sys
import csv

def main():
    check_input()
    tmp = []
    try:
        with open(sys.argv[1]) as before:
            reader =  csv.DictReader(before)
            for row in reader:
                last, first = row["name"].split(", ")
                tmp.append({"first" : first, "last" : last, "house" : row["house"]})
    except:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w") as after:
        writer = csv.DictWriter(after, fieldnames = ["first", "last", "house"] )
        writer.writerow({"first" : "first", "last" : "last", "house" : "house"})
        for row in tmp:
            writer.writerow({"first" : row["first"], "last" : row["last"], "house" : row["house"]})


def check_input():
    if len(sys.argv) < 3:
        sys.exit("Too few  command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

if __name__ == "__main__":
    main()