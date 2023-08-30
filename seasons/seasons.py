from datetime import date
import re
import sys
import inflect
p = inflect.engine()

def main():
    sn = input("Date of Birth: ")
    try:
        ns = check_sn(sn)
    except:
        sys.exit("Invalid date")

    #sn = date(ns["year"], ns["month"], ns["day"])
    print(ns)
    """hn = date.today()
    tg = int((hn-sn).total_seconds()/60)
    out = p.number_to_words(tg, andword = "")"""
    #print(out.capitalize() + " minutes")


def check_sn(sn):
    if match := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", sn):
        ns = {}
        ns["year"] = int(match.group(1))
        ns["month"] = int(match.group(2))
        ns["day"] = int(match.group(3))
        return ns
    

if __name__ == "__main__":
    main()