import random


def main():
    level = get_level()
    score = 0

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y
        guess = None
        wrong_answer = 0

        while True:
            guess = int(input(f"{x} + {y} = "))
            if guess == z:
                score += 1
                break
            else:
                wrong_answer += 1
                print("EEE")
            if wrong_answer == 3:
                print(f"{x} + {y} = {z}")
                break

    print("Score", score)


def get_level():
    while True:
        level = input("Level: ")
        if level.isnumeric() and (0 < int(level) < 4):
            return int(level)


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    else:
        return random.randint(10 ** (level - 1), 10**level)


if __name__ == "__main__":
    main()
