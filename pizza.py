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
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            pizzas.append (row)
        print(tabulate(pizzas, headers ="keys", tablefmt="grid"))
else:
    sys.exit("Not a CSV file")


