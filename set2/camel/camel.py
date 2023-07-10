camelCase = input("camelCase: ")

for i in range(len(camelCase)):
    if camelCase[i].isupper():
        print("_" + camelCase[i].lower(), end="")
    else:
        print(camelCase[i], end="")

print()

