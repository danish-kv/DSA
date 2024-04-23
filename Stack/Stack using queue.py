""" Stack using queue """

from collections import deque
class StackQueue:
    def __init__(self):
        self.q1 = deque()

    def push(self, data):
        self.q1.append(data)
        return print(self.q1)

    def pop(self):
        popped = self.q1.popleft()
        return print(popped, self.q1)


SQ = StackQueue()
SQ.push(10)
SQ.push(20)
SQ.push(30)
SQ.push(40)
SQ.pop()