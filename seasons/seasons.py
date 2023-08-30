from datetime import date
import re
import 
chu = inflect.engine()

def main():
    sn = input("Date of Birth: ")

def check_sn(sn):
    if match := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", sn):
        ns = {}
        ns["year"] = match.group(1)
        ns["month"] = match.group(2)
        ns["day"] = match.group(3)
    else:
        sys.

