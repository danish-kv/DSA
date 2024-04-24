class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None


    def insert(self,data):
        new_node = TreeNode(data)
        current_node = self.root
        if current_node is None:
            self.root = TreeNode(data)
        else:
            while Tree:
                if data < current_node.data:
                    if current_node.left is None:
                        current_node.left = TreeNode(data)
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = TreeNode(data)
                        break
                    else:
                        current_node = current_node.right

    def contains(self,data):
        current_node = self.root
        while current_node is not None:
            if data < current_node.key:
                current_node = current_node.left
            elif data > current_node.key:
                current_node = current_node.right
            else:
                return print('yes')
        return print('Not Contain')








t = Tree()
t.insert(10)
t.insert(20)
t.insert(30)
t.contains(10)

