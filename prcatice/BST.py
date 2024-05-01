class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.key == data:
            print('duplicates not')
            return
        if self.key is None:
            self.key = data
            return
        else:
            if data < self.key:
                if self.lchild:
                    self.lchild.insert(data)
                else:
                    self.lchild = BST(data)
            else:
                if self.rchild:
                    self.rchild.insert(data)
                else:
                    self.rchild = BST(data)

    def search(self,data):
        if self.key is None:
            print('BST is Empty')
            return

        if self.key == data:
            print(data,'founded')
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print('not found')
                return
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print('not found')
                return

    def remove(self,data,curr):
        if self.key is None:
            print('Tree not grown')
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.remove(data,curr)
            else:
                print('Not Present')
                return
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.remove(data,curr)
            else:
                print('not Found')
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.rchild = temp.rchild
                    self.lchild = temp.lchild
                    temp = None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.rchild = temp.rchild
                    self.lchild = temp.lchild
                    temp = None
                    return
                self = None
                return  temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.remove(node.key,curr)
            return self






tree = BST(10)
arr = [12, 5, 8, 3, 4]
for i in arr:
    tree.insert(i)

tree.search(10)
tree.remove(10,tree)
tree.search(10)
