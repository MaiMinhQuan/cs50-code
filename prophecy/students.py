import csv

students = []
houses = []
relationships = []

def creat_house(house, houses):
    count = 0
    for h in houses:
        if h == house :
            count += 1
    if count == 0:
        houses.append(house)

with open("students.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row["student_name"]
        house = row["house"]
        head = row["head"]
        create_house(house, houses)
