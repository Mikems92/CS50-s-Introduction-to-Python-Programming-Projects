from tabulate import tabulate
from os import path
import sys
import csv


if len(sys.argv) < 2 :
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2 :
    sys.exit("Too many command-line arguments")
elif path.exists(sys.argv[1]):
    pass

if sys.argv[1].endswith(".csv") :
    pizzas =[]
    with open("regular.csv") as file:
        reader = csv.reader(file)
        for regular_pizza, small, large in reader:
            pizzas.append ({"Regular Pizza": regular_pizza, "Small": small, "Large": large})
        print(tabulate(pizzas, tablefmt="grid"))
else:
    print("Not a CSV file")


