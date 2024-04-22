""" Find Min value from Stack """


class Stack:
    def __init__(self):
        self.item = []
        self.min_value = []

    def add(self, x):
        self.item.append(x)
        if not self.min_value or x <= self.item[-1]:
            self.min_value.append(x)
        return self.item

    def pop(self):
        if self.item:
            popped = self.item.pop()
            if popped == self.min_value[-1]:
                self.min_value.pop()
            return popped

    def peek(self):
        if self.item:
            return self.item[-1]

    def getMin(self):
        if self.min_value:
            return self.min_value[-1]


S = Stack()
S.add(30)
S.add(60)
S.add(90)
S.add(64)
p = S.add(10)
print('Current List:', p)
print('Current Min Value:-', S.getMin())
S.pop()
print('Current List:', p)
print('Current Min Value:-', S.getMin())
