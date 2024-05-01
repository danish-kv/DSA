class SuffixNode:
    def __init__(self):
        self.child = {}
        self.is_end = False


class SuffixTrie:
    def __init__(self):
        self.root = SuffixNode()

    def build_tree(self, word):
        for i in range(len(word)):
            self.insert(i, word)

    def insert(self, i, word):
        node = self.root
        for j in range(i, len(word)):
            if word[j] not in node.child:
                node.child[word[j]] = SuffixNode()
            node = node.child[word[j]]
        node.is_end = True

    def search(self, word):
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.child:
                return False
            node = node.child[word[i]]
        return True

    def prefix_search(self,word):
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.child:
                return []
            node = node.child[word[i]]

        return self._dfs(node,word)

    def _dfs(self,node,word):
        res = []
        if node.is_end:
            res.append(word)
        for char, child_node in node.child.items():
            res.extend(self._dfs(child_node, word + char))
        return res

    def delete(self,word):
        self.delete_recursive(self.root,word,0)

    def delete_recursive(self,node,word,index):
        if index == len(word):
            node.is_end = False
            return

        letter = word[index]
        if letter not in node.child:
            return

        child_node = node.child[letter]
        self.delete_recursive(child_node,word,index + 1)

        if not child_node.child and child_node.is_end:
            del child_node[letter]



ST = SuffixTrie()
ST.build_tree('danish')
ST.build_tree('da')
ST.build_tree('danishkv')
ST.build_tree('dani')
print(ST.search('danish'))
print('Before deletion:-')
print(ST.prefix_search('da'))
ST.delete('da')
print('After deletion:-')
print(ST.prefix_search('da'))
