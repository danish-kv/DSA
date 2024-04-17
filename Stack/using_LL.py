class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def print(self):
        if self.top is None:
            print('stack is Empty')
        else:
            n = self.top
            while n is not None:
                print(n.data)
                n = n.next

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        data = self.top.data
        self.top = self.top.next
        return print('popped value', data)

    def peek(self):
        return print('Peek Value',self.top.data)

    def size(self):
        count = 0
        n = self.top
        while n:
            count += 1
            n = n.next
        return count

    def delete_middle(self):
        size =  self.size()
        middle = size // 2
        c = 0
        n = self.top
        while n.next is not None:
            c += 1
            if c == middle:
                break
            n = n.next
        n.next = n.next.next



SS = Stack()
SS.push(10)
SS.push(20)
SS.push(30)
SS.push(40)
SS.push(50)
SS.delete_middle()
SS.size()
SS.print()
