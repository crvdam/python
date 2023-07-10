def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return length(s) and start_letters(s) and alpha_num(s) and no_middle_num(s)


def length(s):
    return len(s) >= 2 and len(s) <= 6


def start_letters(s):
    return s[1].isalpha()


def alpha_num(s):
    return s.isalnum()


def no_middle_num(s):
    for i in range(len(s)):
        if s[i].isnumeric():
            if s[i] == "0":
                return False
            elif s[i:len(s)].isnumeric():
                return True
            else:
                return False
    return True

if __name__ == "__main__":
    main()