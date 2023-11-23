from tabulate import tabulate
import csv
import sys
import re
def main():
    #check input
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].endswith(".csv") == False:
        sys.exit("Not a CSV file")

    #list that stores row in csv file
    subjects = []

    #list that stores IDs of subject
    valid_IDs = []
    try:
        with open(sys.argv[1]) as f:
            reader = csv.DictReader(f)
            for subject in reader:
                subjects.append(subject)
                valid_IDs.append(subject["ID"])
    except:
        sys.exit("File does not exist")



    print(tabulate(subjects, headers = {"ID":"ID", "Subject":"Subject", "Day":"Day", "Time":"Time"}, tablefmt = "grid"))
    print()

    #enter name
    while True:
        name = input("PLease enter your real name: ")
        if check_name(name):
            break
        else:
            print("Invalid name")

    #list that stores timetable
    timetable = []
    for i in range(4):
        row = []
        for j in range (8):
            row.append("")
        timetable.append(row)
    timetable[0][1] = "Monday"
    timetable[0][2] = "Tuesday"
    timetable[0][3] = "Wednesday"
    timetable[0][4] = "Thursday"
    timetable[0][5] = "Friday"
    timetable[0][6] = "Saturday"
    timetable[0][7] = "Sunday"
    timetable[1][0] = "Morning"
    timetable[2][0] = "Afternoon"
    timetable[3][0] = "Evening"
    timetable[0][0] = name

    #select subjects
    selected_IDs = []
    print("Please enter subject 's IDs")
    while True:
        try:
            id = input("Subject 's ID: ")
            if id in valid_IDs:
                if id not in selected_IDs:
                    selected_IDs.append(id)
                    for subject in subjects:
                        if id == subject["ID"]:
                            column = day_convert(subject["Day"])
                            if column == "Day is invalid":
                                continue
                            row = time_convert(subject["Time"])
                            if row == "Time is invalid":
                                continue
                            if timetable[row][column] != "":
                                print(f"There is already a registered subject in the time of {subject['Subject']}")
                                answer = ""
                                while answer != "y" and answer != "n":
                                    answer = input(f"Do you still want to register {subject['Subject']}?(y/n) ")
                                if answer == "n":
                                    del selected_IDs[len(selected_IDs)-1]
                                    continue
                                if answer == "y":
                                    for subject1 in subjects:
                                        if subject1["Subject"] == timetable[row][column]:
                                            selected_IDs.remove(subject1["ID"])
                            timetable[row][column] = subject["Subject"]
            else:
                print("ID is not valid")
                continue
        except EOFError:
            print()
            break

    print(tabulate(timetable[1:], headers = timetable[0], tablefmt = "grid"))


def day_convert(day):
    if day == "Monday":
        return 1
    elif day == "Tuesday":
        return 2
    elif day == "Wednesday":
        return 3
    elif day == "Thursday":
        return 4
    elif day == "Friday":
        return 5
    elif day == "Saturday":
        return 6
    elif day == "Sunday":
        return 7
    else:
        return "Day is invalid"

def time_convert(time):
    if time == "Morning":
        return 1
    elif time == "Afternoon":
        return 2
    elif time == "Evening":
        return 3
    else:
        return "Time is invalid"

def check_name(name):
    if re.search(r"^[a-zA-Z][a-zA-Z ]*$", name):
        return True
    else:
        return False


if __name__ == "__main__":
    main()






