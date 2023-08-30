class Jar:
    def __init__(self, capacity = 12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError
        if self.size + n > self.capacity:
            raise ValueError
        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        self.size -= n

    @property
    def capacity(self):
        if 
