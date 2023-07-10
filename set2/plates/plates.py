def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if length(s) and start_letters(s) and alpha_num(s) and no_middle_num(s):
        return True
    else:
        return False


def length(s):
    if len(s) < 2 or len(s) > 6:
        return False
    else:
        return True


def start_letters(s):
    if s[0:1].isalpha():
        return True
    else:
        return False


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


main()