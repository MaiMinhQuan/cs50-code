from tabulate import tabulate
import csv
def main():
    a = []
    b = []
    with open("test.csv") as f:
        reader = csv.DictReader(f)
        for subject in reader:
            a.append(subject)
            b.append(int(subject["ID"]))


    #print(b)
    print(tabulate(a, headers = {"ID":"ID", "Subject":"Subject", "Day":"Day", "Time":"Time"}, tablefmt = "grid"))

    IDs = []
    while True:
        try:
            id = int(input("Subject 's ID: "))
            if id in b:
                if id not in IDs:
                    IDs.append(id)
                    for subject in a:
                        if id == subject["ID"]

            else:
                print("ID is not valid")
                continue
        except EOFError:
            print()
            break

    #IDs.sort()
    #print(IDs)
    for id in IDs:













if __name__ == "__main__":
    main()






