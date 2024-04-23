""" Using Array """

class Queue:
    def __init__(self):
        self.item = []
        self.front = self.rear = 0

    def enqueue(self,data):
        self.item.append(data)

    def dequeue(self):
        self.item.pop(0)


    def print(self):
        for i in self.item:
            print(i,'<--',end=" ")

    def queueFront(self):
        return print(self.item[self.front])







QQ = Queue()
QQ.enqueue(10)
QQ.enqueue(20)
QQ.enqueue(30)
QQ.dequeue()
QQ.queueFront()
QQ.print()

