# #Using Array
# class Stack:
#     def __init__(self,size):
#         self.item = []
#         self.limit = size
#
#     def sizeof(self):
#         return len(self.item)
#
#     def is_empty(self):
#         return len(self.item) == 0
#
#     def is_full(self):
#         return len(self.item) == self.limit
#
#     def append(self,value):
#         if not self.is_full():
#             self.item.append(value)
#             return self.item
#         else:
#             print('Stack Overflow')
#
#     def pop(self):
#         if not self.is_empty():
#             return self.item.pop()
#         else:
#             print('Stack underflow')
#
#     def peek(self):
#         return self.item[-1]
#
#
# S = Stack(5)
# print(S.is_empty())
# print(S.pop())
# print(S.append(10))
# print(S.append(20))
# print(S.append(30))
# print(S.append(40))
#
# print(S.pop())
# print(S.peek())
# print(S.sizeof())


# Find Min value from Stack

# class Stack:
#     def __init__(self):
#         self.item = []
#         self.min_value = []
#
#     def add(self, x):
#         self.item.append(x)
#         if not self.min_value or x <= self.item[-1]:
#             self.min_value.append(x)
#         return self.item
#
#     def pop(self):
#         if self.item:
#             popped = self.item.pop()
#             if popped == self.min_value[-1]:
#                 self.min_value.pop()
#             return popped
#
#     def peek(self):
#         if self.item:
#             return self.item[-1]
#
#     def getMin(self):
#         if self.min_value:
#             return self.min_value[-1]
#
#
# S = Stack()
# S.add(30)
# S.add(60)
# S.add(90)
# S.add(64)
# p = S.add(10)
# print(p)
# print(S.getMin())
# S.pop()
# print(S.getMin())
# print(p)
#


# String revsered using stack

class Stack:
    def __init__(self):
        self.items =[]

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
            print('check')
            while not stack.is_empty():
                new_stack.append(stack.pop())

    p = ' '.join(new_stack)
    print(p)



name = 'my name is muhammed danish'
p=rev_string(name)
# print(p)






# using linked list
# class StackNode:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
# class Stack:
#     def __init__(self):
#         self.top = None
#
#     def is_empty(self):
#         return self.top is None
#
#     def print(self):
#         if self.top is None:
#             print('stack is empty')
#         else:
#             n = self.top
#             while n is not None:
#                 print(n.data)
#                 n = n.next
#
#     def push(self,data):
#         new_node = StackNode(data)
#         new_node.next = self.top
#         self.top = new_node
#
#     def pop(self):
#         if not self.is_empty():
#             popped = self.top.data
#             self.top = self.top.next
#             return print('popped value', popped)
#         return None
#
#     def peek(self):
#         return print('peek value: ',self.top.data)
#
#
#
#
# SS = Stack()
# SS.push(10)
# SS.push(20)
# SS.push(30)
# SS.push(40)
# SS.pop()
# SS.pop()
# SS.peek()
# SS.print()




# Stack using queue
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