import inflect
names = []

p = inflect.engine()

while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        adieu = p.join(names)
        print(f"Adieu, adieu, to {adieu}")
        break