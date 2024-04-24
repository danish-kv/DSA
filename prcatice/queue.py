# Using Array

# class Queue:
#     def __init__(self):
#         self.item = []
#         self.front = self.rear = 0
#
#     def enqueue(self,data):
#         self.item.append(data)
#
#     def dequeue(self):
#         self.item.pop(0)
#
#
#     def print(self):
#         for i in self.item:
#             print(i,'<--',end=" ")
#
#     def queueFront(self):
#         return print(self.item[self.front])
#
#
#
#
#
#
#
# QQ = Queue()
# QQ.enqueue(10)
# QQ.enqueue(20)
# QQ.enqueue(30)
# QQ.dequeue()
# QQ.queueFront()
# QQ.print()




# Using LinkedList

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self,data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        self.front = self.front.next

    def print(self):
        n = self.front
        while n is not None:
            print(n.key, '<--', end=" ")
            n = n.next



Q = Queue()
Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(30)
Q.dequeue()
Q.print()