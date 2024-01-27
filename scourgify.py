import sys
import csv
from os import path

x = ""
file = open(sys.argv[2],"w")
file.write(x)
file.close()

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
with open("before.csv") as file:
    reader = csv.reader(file)
    for name, house in reader:
        first_last = name.lstrip('"').rstrip('"').replace(" ","")
        fl.append(first_last)
    fl.pop(0)
with open("after.csv", "a") as file:
    dw = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    dw.writeheader()
    for i in fl:
        first, last = i.split(",")
        dw.writerow({"first":first, "last":last, "house":house})


