from tabulate import tabulate
import csv
def main():
    #list that stores row in csv file
    a = []
    #list that stores IDs of subject
    b = []
    with open("test.csv") as f:
        reader = csv.DictReader(f)
        for subject in reader:
            a.append(subject)
            b.append(int(subject["ID"]))

    #print(a)
    #print(b)
    #print(tabulate(a, headers = {"ID":"ID", "Subject":"Subject", "Day":"Day", "Time":"Time"}, tablefmt = "grid"))

    #list that stores timetable
    IDs = []
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
    while True:
        try:
            id = int(input("Subject 's ID: "))
            if id in b:
                if id not in IDs:
                    IDs.append(id)
                    for subject in a:
                        if id == int(subject["ID"]):
                            column = day_convert(subject["Day"])
                            row = time_convert(subject["Time"])
                            timetable[row][column] = subject["Subject"]
            else:
                print("ID is not valid")
                continue
        except EOFError:
            print()
            break

    #IDs.sort()
    #print(IDs)
    #print(time_convert("Afternoon"))
    #print(timetable)
    print(tabulate(timetable, tablefmt = "grid"))


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

def table(r, c):
    table = []

    return table



if __name__ == "__main__":
    main()






