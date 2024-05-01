class PrefixNode:
    def __init__(self):
        self.child = {}
        self.is_end = False

class PrefixTrie:
    def __init__(self):
        self.root = PrefixNode()

    def insert(self,word):
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.child:
                node.child[word[i]] = PrefixNode()
            node = node.child[word[i]]
        node.is_end = True

    def search(self,word):
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.child:
                return False
            node = node.child[word[i]]
        return node.is_end

    def prefix_search(self,word):
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.child:
                return []
            node = node.child[word[i]]
        return self.prefix_search_helper(node,word)

    def prefix_search_helper(self,node,word):
        res = []
        if node.is_end:
            res.append(word)

        for char, child_node in node.child.items():
            res.extend(self.prefix_search_helper(child_node,word+char))

        return res

    def remove(self,word):
        self.removeHelper(self.root,word,0)

    def removeHelper(self,node,word,index):
        if index == len(word):
            node.is_end = False
            return

        letter = word[index]
        if letter not in node.child:
            return

        child_node = node.child[letter]
        self.removeHelper(child_node,word,index + 1)

        if not child_node.child and not child_node.is_end:
            del child_node[letter]






A = PrefixTrie()
A.insert('danish')
A.insert('da')
A.insert('dai')
A.insert('sha')
print(A.search('da'))
print(A.prefix_search('da'))
A.remove('da')
print('after deletion')
print(A.prefix_search('da'))