import re
import sys
sn = input("Birthday: ")
if match := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", sn):
    ns = {}
    ns["year"] = int(match.group(1))
    ns["month"] = int(match.group(2))
    ns["day"] = int(match.group(3))
    print(ns)
else:
    sys.exit("Invalid")
