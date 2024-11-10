def main():
    jar_01 = Jar()
    jar_01.deposit(4)
    jar_01.withdraw(1)
    print(jar_01)


class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity in a negative integer")

        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):

        if self.capacity < n or self.size + n > self.capacity:
            raise ValueError("Capacity exceded")

        else:
            self._size += n

    def withdraw(self, n):

        if self.size - n < 0 or self.size < n:
            raise ValueError("There is no cookies in the Jar")

        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


if __name__ == "__main__":
    main()
