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

    #print(a)
    #print(b)
    #print(tabulate(a, headers = {"ID":"ID", "Subject":"Subject", "Day":"Day", "Time":"Time"}, tablefmt = "grid"))

    IDs = []
    timetable = table_0(3,7)
    #print(timetable)
    while True:
        try:
            id = int(input("Subject 's ID: "))
            if id in b:
                if id not in IDs:
                    IDs.append(id)
                    for subject in a:
                        if id == subject["ID"]:
                            column = day_convert(subject["Day"])
                            row = time_convert(subject["Time"])
                            print(row, column)
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


def day_convert(day):
    if day == "Monday":
        return 0
    elif day == "Tuesday":
        return 1
    elif day == "Wednesday":
        return 2
    elif day == "Thursday":
        return 3
    elif day == "Friday":
        return 4
    elif day == "Saturday":
        return 5
    elif day == "Sunday":
        return 6

def time_convert(time):
    if time == "Morning":
        return 0
    elif time == "Afternoon":
        return 1
    elif time == "Evening":
        return 2

def table_0(r, c):
    table = []
    for i in range(r):
        row = []
        for j in range (c):
            row.append(0)
        table.append(row)
    return table



if __name__ == "__main__":
    main()






