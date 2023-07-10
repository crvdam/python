import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    url = re.search(r"\"(https?://)?(www\.)?youtube\.com/embed/(.+)\"", s)
    if url:
        return(f"https://youtu.be/{url.group(3)}")




if __name__ == "__main__":
    main()