question = input(">").lower().lstrip().rstrip()

if question == "42" or question == "forty-two" or question == "forty two":
    print("Yes")
else:
    print("No")