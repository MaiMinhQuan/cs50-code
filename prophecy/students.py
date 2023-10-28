import csv

def creat_house(house, houses, head):
    count = 0
    for h in houses:
        if h["house"] == house :
            count += 1
    if count == 0:
        houses.append({"house": house, "head": head})

def creat_student(name, students):
    students.append({"student_name": name})

def create_relationship(name, house, relationship):
    
students = []
houses = []
relationships = []


with open("students.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row["student_name"]
        house = row["house"]
        head = row["head"]

        create_house(house, houses, head)
        create_student(name, students)
