from tabulate import tabulate
import csv
import sys
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
                valid_IDs.append(int(subject["ID"]))
    except:
        sys.exit("File does not exit")


    #print(b)
    print(tabulate(subjects, headers = {"ID":"ID", "Subject":"Subject", "Day":"Day", "Time":"Time"}, tablefmt = "grid"))

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
    #print(timetable)


    #select subjects
    selected_IDs = []
    print("Please enter subject 's IDs")
    while True:
        try:
            id = int(input("Subject 's ID: "))
            if id in valid_IDs:
                if id not in selected_IDs:
                    selected_IDs.append(id)
                    for subject in subjects:
                        if id == int(subject["ID"]):
                            column = day_convert(subject["Day"])
                            row = time_convert(subject["Time"])
                            if timetable[row][column] != "":
                                print(f"There is already a registered subject in the time of {subject['Subject']}")
                                answer = input(f"Do you still want to register {subject['Subject']}?(y/n) ")
                                if answer == "n":
                                    continue
                                if answer != "y":
                                    print("The answer must be 'y' or 'n'")
                            timetable[row][column] = subject["Subject"]
            else:
                print("ID is not valid")
                continue
        except EOFError:
            print()
            break

    #IDs.sort()
    #print(selected_IDs)
    #print(timetable)
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

def time_convert(time):
    if time == "Morning":
        return 1
    elif time == "Afternoon":
        return 2
    elif time == "Evening":
        return 3



if __name__ == "__main__":
    main()






