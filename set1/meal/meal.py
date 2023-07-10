def main():
    convertedTime = convert(input("What time is it? "))
    if 7 <= convertedTime <= 8:
        print("breakfast time")
    elif 12 <= convertedTime <= 13:
        print("lunch time")
    elif 18 <= convertedTime <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")

    if "a.m." in time or "p.m." in time:
        minutes, daynight = minutes.split(" ")

        if daynight == "p.m.":
            hours = int(hours) + 12

    return(int(hours) + int(minutes) / 60)


if __name__ == "__main__":
    main()