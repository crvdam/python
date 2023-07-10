list = {}

while True:
    try:
        item = input().lower()

        if item in list:
            list[item] = list[item] + 1
        else:
            list[item] = 1

    except EOFError:
        sorted_list = sorted(list)
        for i in sorted_list:
            print(list[i], i.upper())
        break


