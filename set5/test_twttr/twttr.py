def main():
    invoer = input("Input: ")
    print("Output:",shorten(invoer))


def shorten(woord):
    verkort_woord = ""
    for i in range(len(woord)):
        if woord[i] in "aeiou":
            continue
        else:
            verkort_woord += woord[i]
    return verkort_woord


if __name__ == "__main__":
    main()