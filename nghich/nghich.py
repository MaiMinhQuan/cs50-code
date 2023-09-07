from tabulate import tabulate
import csv
def main():
    with open("test.csv") as f:
        a = []
        reader = csv.reader(f)
        for row in reader:
            a.append(row)

    print(tabulate(a[1:], headers = a[0], tablefmt = "grid"))

    


