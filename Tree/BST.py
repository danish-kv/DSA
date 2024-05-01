class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if data == self.key:
            return print('Duplicate not allowed in BST')

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

    def search(self, data):
        if self.key is None:
            return "BST is Empty"

        if self.key == data:
            return f'{data} contain in BST'

        if self.key > data:
            if self.lchild is not None:
                return self.lchild.search(data)
            else:
                return 'Not Contain'

        else:
            if self.rchild is not None:
                return self.rchild.search(data)
            else:
                return 'Not Contain'

    def contain(self, data):
        current = self
        while current:
            if current.key == data:
                return f"{data} found in BST"
            elif data < current.key:
                current = current.lchild
            else:
                current = current.rchild
        return 'Not Found'

    def preorder(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()

        print(self.key, end=" ")

        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()

        if self.rchild:
            self.rchild.postorder()

        print(self.key, end=" ")

    def remove(self, data, curr):
        if self.key is None:
            print('BST is Empty')
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.remove(data, curr)
            else:
                print('Not Found')

        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.remove(data, curr)
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.remove(node.key, curr)
            return self

    def count(self, node):
        if node is None:
            return 0
        return 1 + self.count(node.lchild) + self.count(node.rchild)

    def min_node(self):
        curr = self
        while curr.lchild:
            curr = curr.lchild
        print('Min:-', curr.key)
        return

    def max_node(self):
        curr = self
        while curr.rchild:
            curr = curr.rchild
        print('Max:-', curr.key)
        return

    def min_node_using_recurion(self):
        if self.lchild:
            self.lchild.min_node_using_recurion()
        elif self.lchild is None:
            print('min is ', self.key)


arr = [12, 8, 3, 98, 45]
tree = BST(10)
for i in arr:
    tree.insert(i)

print(tree.search(8))
print(tree.search(10))
print('Pre Order')
tree.preorder()
print('\nIn order')
tree.inorder()
print('\nPost Order')
tree.postorder()
print()
if tree.count(tree) > 1:
    tree.remove(10, tree.key)
else:
    print("Can't perform delete opretion")
print('After deletetion opretion')
tree.preorder()
print()
tree.min_node()
tree.max_node()
