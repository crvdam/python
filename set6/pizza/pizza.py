import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")

try:
    menu = []
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            menu.append(row)
    print(menu)
    print(tabulate(menu, tablefmt="grid", headers="firstrow"))


except FileNotFoundError:
    sys.exit("File does not exist")