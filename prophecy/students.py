import csv
from cs50 import SQL

def creat_house(house, houses, head):
    count = 0
    for h in houses:
        if h["house"] == house :
            count += 1
    if count == 0:
        houses.append({"house": house, "head": head})

def creat_student(name, students):
    students.append({"student_name": name})

def create_relationship(name, house, relationships):
    relationships.append({"student_name": name, "house": house})

db = SQL("sqlite:///roster.db")

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
        create_relationship(name, house, relationships)

for student in students:
    db.execute("INSERT INTO new_students (student_name) VALUE ?", student["student_name"])

for r in relationships:
    db.execute("INSERT INTO relationship (student_name, house) VALUE (?, ?)", r["student_name"], r["house"])

for house in houses:
    db.execute("INSERT INTO houses (house, head) VALUE (?, ?)", house["house"], house["head"])