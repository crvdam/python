import re
import sys


def main():
    while True:
        print(validate(input("IPv4 Address: ")))


def validate(ip):
    m = re.search(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)
    try:
        for i in range(1,5):
            if 0 < int(m.group(i)) > 255:
                return False
        return True

    except AttributeError:
        return False

if __name__ == "__main__":
    main()