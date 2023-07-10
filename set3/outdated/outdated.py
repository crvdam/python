maanden = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    try:
        datum = input("Date: ")
        if "/" in datum:
            maand, dag, jaar = datum.split(sep="/")
        elif ", " in datum:
            maand, dag, jaar = datum.split(sep=" ")
            dag = dag.rstrip(",")
            maand = (maanden.index(maand)) + 1
        else:
            continue
        if int(dag) > 31 or int(maand) > 12 or int(jaar) > 9999:
            continue
        print(f"{int(jaar)}-{int(maand):02}-{int(dag):02}")
        break
    except ValueError:
        continue
