class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.nref = None


class DoublyLL:
    def __init__(self):
        self.head = None

    def print(self):
        check = []
        if self.head is None:
            print("LL is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,'-->', end=" ")
                n = n.nref

    def print_rev(self):
        print()
        if self.head is None:
            print('LL is Empty')
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.prev

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('Not Empty')

    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.prev = n

    def add_after(self, data, pos):
        if self.head is None:
            print('LL is Empty')
            return
        if pos == self.head.data:
            new_node = Node(data)
            new_node.nref = self.head.nref
            new_node.prev = self.head
            self.head.nref.prev = new_node
            self.head.nref = new_node
        else:
            n = self.head
            while n is not None:
                if pos == n.data:
                    break
                n = n.nref

            if n is None:
                print('Not Found')
                return

            new_node = Node(data)
            new_node.nref = n.nref
            if n.nref is not None:
                n.nref.prev = new_node
            n.nref = new_node
            new_node.prev = n

    def add_before(self, data,pos):
        new_node = Node(data)
        if self.head is None:
            print('ll not found')
            return
        if pos == self.head.data:
            new_node.nref = self.head
            self.head.prev = new_node
            self.head = new_node

        else:
            n = self.head
            while n is not None:
                if pos == n.nref.data:
                    break
                n = n.nref

            if n is None:
                print('Not Found')
            else:
                new_node.nref = n.nref
                new_node.prev = n
                if n.prev is not None:
                    n.nref.prev = new_node
                else:
                    self.head = new_node
                n.nref = new_node

    def delete_begin(self):
        if self.head is None:
            print('LL is Empty')
            return
        if self.head.nref is None:
            self.head = None
            print('1st Node deleted')
        else:
            self.head = self.head.nref
            self.head.prev = None

    def delete_end(self):
        if self.head is None:
            print("LL IS EMPTY")
            return
        if self.head.nref is None:
            self.head = None
            print('1st Node deleted')
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.prev.nref = None
    def delete_by_value(self,pos):
        if self.head is None:
            print('LL is Empty')

        if self.head.nref is None:
            if pos == self.head.data:
                self.head = None
                return
            else:
                print('data not found')
            return

        if pos == self.head.data:
            self.head = self.head.nref
            self.head.prev = None
            return
        n = self.head
        while n.nref is not None:
            if pos == n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.nref.prev = n.prev
            n.prev.nref = n.nref
        else:
            if n.data == pos:
                n.prev.nref = None
            else:
                print('not found')


DLL = DoublyLL()
DLL.add_begin(10)
DLL.add_begin(20)
DLL.add_begin(30)
DLL.add_begin(40)
DLL.delete_by_value(10)
DLL.print()

