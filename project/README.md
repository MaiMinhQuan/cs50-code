# Timetable making
#### Video Demo :  <https://www.google.com/>
#### Description:
My program helps students create their own schedules, making studying easier for them.

The file "project.py" contains the main program to help students organize their timetables.

The file "requirements.txt" contains the libraries that need to be installed.

The file "test_project.py" contains test functions.

The file "schedule.csv" contains information about the school's subjects, including ID, name, day, session (Morning, Afternoon, Evening) of the subject (Note: students can only study one subject in a session).

In the file called "project.py", the program that expects exactly one command-line argument, the name (or path) of a CSV file that contains ID, name, date, session of subjects. If user enters too many arguments, "Too many command-line arguments" will appear. If user enters too few arguments, "Too few command-line arguments" will appear. If argument
is not a csv file, "Not a CSV file" will appear. If it is a csv file that does not exist, "File does not exist" will appear.

Next, user needs to enter their real name (not a nickname). If user enters an invalid name, user will have to re-enter the name.

Then, users need to enter the ID of the subjects they want to study.
If the user enters the wrong ID they will have to re-enter it. If the user enters a subject that overlaps with another subject, the user will have to confirm whether the user continues to register for that subject or not. Answer "y" if you still want to register, answer "n" if you do not want to register. If the user's answer is different from "y" and "n", the user will have to answer again.

If the user wants to end the registration process, press "CTRL+D" and the user's schedule will appear
