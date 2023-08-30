from datetime import date
import re
import sys
import inflect
chu = inflect.engine()

def main():
    sn = input("Date of Birth: ")
    ns = check_sn(sn)
    print(ns)
    sn = date(ns["year"], ns["month"], ns["day"])
    hn = date.today()
    tg = (hn - sn) * 24 * 60
    out = chu.number_to_words(tg, andword = "")
    #print(out.capitalize() + "minutes")


def check_sn(sn):
    if match := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", sn):
        ns = {}
        ns["year"] = int(match.group(1))
        ns["month"] = int(match.group(2))
        ns["day"] = int(match.group(3))
        return ns
    else:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()