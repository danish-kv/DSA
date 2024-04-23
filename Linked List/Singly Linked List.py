# Implementing a singly linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print('LL is Empty')
        else:
            n = self.head
            while n is not None:
                print(n.data, '-->', end=" ")
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data, pos):
        n = self.head
        while n is not None:
            if pos == n.data:
                break
            n = n.ref

        if n is None:
            print('Position Not found')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, pos):
        if pos == self.head.data:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return

        n = self.head
        while n.ref is not None:
            if pos == n.ref.data:
                break
            n = n.ref

        if n.ref is None:
            print("Position not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('LL is Not Empty')

    def remove_begin(self):
        if self.head is None:
            print('LL is Empty')
        else:
            self.head = self.head.ref

    def remove_end(self):
        if self.head is None:
            print('LL is Empty')
        else:
            n = self.head
            while n.ref is None:
                n = n.ref
            n.ref = None

    def remove_any(self, pos):
        if self.head is None:
            print("Its Empty")
            return

        if pos == self.head.data:
            self.head = self.head.ref
        else:
            n = self.head
            while n.ref is not None:
                if pos == n.ref.data:
                    break
                n = n.ref

            if n is None:
                print('Not Found')
            else:
                n.ref = n.ref.ref

    def index_of(self, pos):
        if self.head is None:
            print("LL is NUll")
            return
        n = self.head
        index = -1
        while n is not None:
            index += 1
            if pos == n.data:
                break
            n = n.ref
        if n.ref is None:
            print('Not Found')
        else:
            print(index)

    def size(self):
        n = self.head
        size = 0
        while n is not None:
            size += 1
            n = n.ref
        print(size)

    def is_empty(self):
        return self.head is None

    def clear(self):
        self.head = None

    def array_to_ll(self, arr):
        n = self.head
        while n.ref is not None:
            n = n.ref

        for data in arr:
            n.ref = Node(data)
            n = n.ref


LL = LinkedList()
LL.add_begin(10)
LL.add_begin(15)
LL.add_end(20)
LL.add_before(25, 15)
LL.add_after(30, 15)
# LL.index_of(15)
# LL.size()
# LL.is_empty()
# LL.clear()
# LL.insert_empty(100)
LL.array_to_ll([1, 2, 3, 4])
LL.print()
