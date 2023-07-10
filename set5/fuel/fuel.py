def main():
    percentile = convert(input("Fraction: "))
    print(gauge(percentile))


def convert(fraction):
    x, y = fraction.split(sep="/")

    if int(y) == 0:
        raise ZeroDivisionError
    elif x.isnumeric() and y.isnumeric and int(x) <= int(y):
        return round(int(x) / int(y) * 100)
    else:
        raise ValueError

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()