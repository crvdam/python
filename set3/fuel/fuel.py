while True:
    try:

        x, y = input("Fraction: ").split(sep="/")
        if int(x) > int(y):
            continue

        result =  round(int(x) / int(y) * 100)

        if result <= 1:
            print("E")
        elif result >= 99:
            print("F")
        else:
            print(f"{result}%")
        break

    except (ValueError, ZeroDivisionError):
        continue
