from tabulate import tabulate
import csv
with open("test.csv") as f:
    a = []
    reader = csv.reader(f)
    for row in reader:
        a.append(row)

print(tabulate(a, tablefmt = "grid"))


