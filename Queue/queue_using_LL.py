# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class Queue:
#     def __init__(self):
#         self.front = None
#         self.rear = None
#
#     def is_empty(self):
#         return self.front is None
#
#     def print(self):
#         if self.front is None:
#             print('Queue is empty')
#             return
#         n = self.front
#         while n is not None:
#             print(n.data)
#             n = n.next
#
#     def enque(self,data):
#         new_node = Node(data)
#         if self.is_empty():
#             self.front = new_node
#             self.rear = new_node
#         else:
#             self.rear.next = new_node
#             self.rear = new_node
#
#     # def dequeue(self):
#     #     i
#
#
#
# Q = Queue()
# Q.enque(10)
# Q.enque(20)
# Q.enque(30)
# Q.enque(40)
#
# Q.print()
#
