from tabulate import tabulate
import csv
def main():
    a = []
    b = []
    with open("test.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            a.append(row)
            b.append(int(row["ID"]))


    #print(b)
    print(tabulate(a, tablefmt = "grid"))

    """IDs = []
    while True:
        try:
            id = int(input("Subject 's ID: "))
            if id in b:
                if id not in IDs:
                    IDs.append(id)
            else:
                print("ID is not valid")
                continue
        except EOFError:
            print()
            break

    print(IDs)
    IDs.sort()
    print(IDs)"""













if __name__ == "__main__":
    main()






