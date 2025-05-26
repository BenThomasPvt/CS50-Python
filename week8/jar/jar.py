class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self.capacity = capacity
        self.cookies = 0  # Starts with 0 cookies in the jar

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        if n < 0:
            raise ValueError("Cannot deposit a negative number of cookies.")
        if self.cookies + n > self.capacity:
            raise ValueError("Cannot exceed the jar's capacity.")
        self.cookies += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cannot withdraw a negative number of cookies.")
        if self.cookies < n:
            raise ValueError("Not enough cookies to withdraw.")
        self.cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = value

    @property
    def size(self):
        return self.cookies
