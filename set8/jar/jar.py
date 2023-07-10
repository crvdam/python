import sys

class Jar:
    def __init__(self, capacity=12):

        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        self._size += n
        if self.size > self._capacity:
            raise ValueError("This will exceed the jar's capacity")

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not enough cookies in the jar-o")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        self._size = n


def main():
    jar = Jar()

    while True:
        print("What would you like to do?\n1. deposit | 2. withdraw | 3. balance | 4. exit")
        action = input(">")
        if action == "1":
            jar.deposit(int(input("Amount: ")))
        elif action == "2":
            jar.withdraw(int(input("Amount: ")))
        elif action == "3":
            print(jar)
        elif action == "4":
            sys.exit()
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()