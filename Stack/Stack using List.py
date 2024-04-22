#Using Array
class Stack:
    def __init__(self,size):
        self.item = []
        self.limit = size

    def sizeof(self):
        return len(self.item)

    def is_empty(self):
        return len(self.item) == 0

    def is_full(self):
        return len(self.item) == self.limit

    def append(self,value):
        if not self.is_full():
            self.item.append(value)
            return self.item
        else:
            print('Stack Overflow')

    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            print('Stack underflow')

    def peek(self):
        return self.item[-1]


S = Stack(5)
print(S.is_empty())
print(S.pop())
print(S.append(10))
print(S.append(20))
print(S.append(30))
print(S.append(40))

print(S.pop())
print(S.peek())
print(S.sizeof())
