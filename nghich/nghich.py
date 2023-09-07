from tabulate import tabulate
import csv
def main():
    with open("test.csv") as f:
        a = []
        reader = csv.reader(f)
        for row in reader:
            a.append(row)


    print(a)
    print(tabulate(a[1:], tablefmt = "grid"))

    """"IDs = []
    while True:
        try:
            id = input("Subject 's ID: ")
            if id not in IDs:
                IDs.append(id)"""
main()






