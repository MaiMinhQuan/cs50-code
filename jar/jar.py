class Jar:
    def __init__(self, capacity = 12):
        if self.capacity < 0:
            raise ValueError
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return ""