from datetime import date
import re
import sys
import inflect
p = inflect.engine()

def main():
    sn = input("Date of Birth: ")
    ns = check_sn(sn)

    sn = date(ns["year"], ns["month"], ns["day"])
    hn = date.today()
    tg = int((hn - sn) * 24 * 60)
    print(tg)
    print(type(tg))
    #out = p.number_to_words(tg)
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