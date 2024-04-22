"""
String reversing using stack
my name is muhammed danish -->  ym eman si demmahum hsinad
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


def rev_string(word1):
    stack = Stack()
    new_stack = []
    for i in word1:
        stack.push(i)
        if i == ' ':
            while not stack.is_empty():
                new_stack.append(stack.pop())

    p = ' '.join(new_stack)
    print(p.strip())


name = 'my name is muhammed danish'
rev_string(name)
