import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time = re.search(r"(\d?\d+):?(\d\d)? (AM|PM)+ to (\d?\d+):?(\d\d)? (AM|PM)+", s, re.IGNORECASE)
    if time:
        hour_1 = int(time.group(1))
        hour_2 = int(time.group(4))
        minute_1 = 0
        minute_2 = 0

        if hour_1 > 12 or hour_2 > 12:
            raise ValueError

        if time.group(2):
            minute_1 = int(time.group(2))
            if minute_1 > 59:
                raise ValueError

        if time.group(5):
            minute_2 = int(time.group(5))
            if minute_2 > 59:
                raise ValueError

        if time.group(3).upper() == "PM" and hour_1 != 12:
            hour_1 += 12
        elif time.group(3).upper() == "AM" and hour_1 == 12:
            hour_1 = 0

        if time.group(6).upper() == "PM" and hour_2 != 12:
            hour_2 += 12
        elif time.group(6).upper() == "AM" and hour_2 == 12:
            hour_2 = 0


        return (f"{hour_1:02}:{minute_1:02} to {hour_2:02}:{minute_2:02}")

    else:
        raise ValueError


if __name__ == "__main__":
    main()


