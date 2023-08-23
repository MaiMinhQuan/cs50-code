from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

f = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(f))
elif len(sys.argv) == 3 and (sys.argv[1] == "f" or sys.argv[1] == "--font") and sys.argv[2] in f:
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid usage")

s = input("Input: ")
print(figlet.renderText(s))