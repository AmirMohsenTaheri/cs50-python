import sys
import csv
from tabulate import tabulate

if len(sys.argv) == 2:

    if sys.argv[1].endswith(".csv"):

        try:
            pizza = []
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                for row in reader:
                    pizza.append(row)
                print(tabulate(pizza, headers="firstrow", tablefmt="grid"))
        except(FileNotFoundError):
            sys.exit("File does not exist")

    else:
        sys.exit("Not a Python file")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments ")

elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
