import re
import sys


def main():
    # LOOP VERWIJDEREN!!!
    while True:
        print(count(input("Text: ")))


def count(s):
    n = (re.findall(r"\bum\b", s, re.IGNORECASE))
    return(len(n))



if __name__ == "__main__":
    main()