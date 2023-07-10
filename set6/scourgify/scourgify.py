import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Could not read invalid_file.csv")

try:
    students = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"last": row["name"].split(",")[0], "first": row["name"].split(", ")[1], "house": row["house"]})

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in students:
            writer.writerow(row)





except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")