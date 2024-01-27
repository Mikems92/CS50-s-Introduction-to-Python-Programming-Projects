import sys
import csv
from os import path

x = ""
file = open(sys.argv[2],"w")
file.write(x)


if len(sys.argv) < 3 :
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3 :
    sys.exit("Too many command-line arguments")

if path.exists(sys.argv[1]) :
    if path.exists(sys.argv[2]):
        pass
    else :
        sys.exit(f"Could not read {sys.argv[2]}")
else:
    sys.exit(f"Could not read {sys.argv[1]}")

fl = []
flh = []
with open(sys.argv[1]) as file:
    reader = csv.reader(file)
    for name, house in reader:
        last_first = name.strip('"')
        fl.append(last_first)
    fl.pop(0)
with open(sys.argv[2], "w", newline = '') as file:
    dw = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    dw.writeheader()
    for i in fl:
        last, first = i.split(", ")
        dw.writerow({"first":first.strip(), "last":last.strip(), "house":house.strip()})


