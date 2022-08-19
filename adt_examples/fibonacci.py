class Fib:
    def __init__(self, value1=0, value2=1, next=None):
        self.v1 = value1
        self.v2 = value2
        self.next = next

    def __iter__(self):
        return self

    def __next__(self):
        next = self.v1 + self.v2
        self.v1 = self.v2
        self.v2 = next
        return self.v2
