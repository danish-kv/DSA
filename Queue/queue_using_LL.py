class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def display(self):
        if self.front is None:
            print('Queue is empty')
            return
        n = self.front
        while n is not None:
            print(n.data, '<--', end=" ")
            n = n.next

    def enqueue(self, data):
        new_node = Node(data)
        if self.front  is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front.next is None:
            self.front = self.rear = None
        else:
            self.front = self.front.next


QQ = Queue()
QQ.enqueue(10)
QQ.enqueue(20)
QQ.enqueue(30)
QQ.dequeue()
QQ.display()


