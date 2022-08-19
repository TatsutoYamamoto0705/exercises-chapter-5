from numbers import Number
import operator
import math


class RPCalc:
    def __init__(self, lis=[]):
        self.list = lis
        self.len = 0

    def push(self, par):
        if isinstance(par, Number):
            self.list += [par]
            self.len += 1
        else:
            if len(par) == 1:
                ops = {"+": operator.add,
                       "-": operator.sub,
                       "*": operator.mul,
                       "/": operator.truediv}

                op1 = self.list.pop()
                op2 = self.list.pop()
                self.list.append(ops[par](op2, op1))
                self.len -= 1
            else:
                if hasattr(math, par):
                    op1 = self.list.pop()
                    self.list.append(getattr(math, par)(op1))

    def pop(self):
        self.list.pop()
        self.len += -1

    def peek(self):
        return self.list[-1]

    def __len__(self):
        return self.len
