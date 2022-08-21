class Deque:
    def __init__(self, n):
        self.list = [None] * n
        self.dequelength = n
        self.length = 0
        self.lpointer = 0
        self.rpointer = 0

    def append(self, par):
        self.list[self.rpointer % self.dequelength] = par
        self.rpointer += 1
        self.length += 1

    def appendleft(self, par):
        self.list[(self.lpointer - 1) % self.dequelength] = par
        self.lpointer -= 1
        self.length += 1

    def pop(self):
        returnval = self.list[(self.rpointer - 1) % self.dequelength]
        self.list[(self.rpointer - 1) % self.dequelength] = None
        self.rpointer -= 1
        self.length -= 1
        return returnval

    def popleft(self):
        returnval = self.list[self.lpointer % self.dequelength]
        self.list[self.lpointer % self.dequelength] = None
        self.lpointer += 1
        self.length -= 1
        return returnval

    def peek(self):
        return self.list[(self.rpointer - 1) % self.dequelength]

    def peekleft(self):
        return self.list[self.lpointer % self.dequelength]

    def __len__(self):
        return self.length

    def __iter__(self):
        return DequeIterator(self)


class DequeIterator():
    def __init__(self, deque):
        self.here = deque

    def __iter__(self):
        return self

    def __next__(self):
        if self.here.list[self.here.lpointer % self.here.dequelength]:
            next = self.here.list[self.here.lpointer % self.here.dequelength]
            self.here.lpointer += 1
            if self.here.lpointer != self.here.rpointer + 1:
                return next
            else:
                raise StopIteration

        else:
            raise StopIteration
