def main():
    greeting = input(">")
    print(f"${value(greeting)}")


def value(greeting):
    greeting = greeting.lower().lstrip().rstrip
    if greeting == ("wat moet je?"):
        return 0
    if greeting.startswith("hello"):
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()





