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


    #print(b)
    #print(tabulate(a, headers = {"ID":"ID", "Subject":"Subject", "Day":"Day", "Time":"Time"}, tablefmt = "grid"))

    IDs = []
    timetable = [[""] * 7] * 3
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
                            timetable[row][column] = subject["Subject"]




            else:
                print("ID is not valid")
                continue
        except EOFError:
            print()
            break

    #IDs.sort()
    #print(IDs)
    timetable[0][0] = "Hello"
    print(timetable)


def day_convert(day):
    if day == "Monday":
        return 0
    if day == "Tuesday":
        return 1
    if day == "Wednesday":
        return 2
    if day == "Thursday":
        return 3
    if day == "Fridayday":
        return 4
    if day == "Saturday":
        return 5
    if day == "Sunday":
        return 6

def time_convert(time):
    if time == "Morning":
        return 0
    if time == "Afternoon":
        return 1
    if time == "Evening":
        return 2














if __name__ == "__main__":
    main()






