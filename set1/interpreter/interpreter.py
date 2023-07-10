x, y, z = input(">").split(" ")

x = int(x)
z = int(z)

if y == "+":
    print("{:.1f}".format(x + z))
elif y == "-":
    print("{:.1f}".format(x - z))
elif y == "*":
    print("{:.1f}".format(x * z))
elif y == "/":
    print("{:.1f}".format(x / z))