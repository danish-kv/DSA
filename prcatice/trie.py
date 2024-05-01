# class Node:
#     def __init__(self):
#         self.child = {}
#         self.is_end = False
#
# class PrefixTree:
#     def __init__(self):
#         self.root = Node()
#
#     def insert(self,word):
#         node = self.root
#
#         for i in word:
#             if i not in node.child:
#                 node.child[i] = Node()
#             node = node.child[i]
#         node.is_end = True
#
#     def search(self,word):
#         node = self.root
#         for i in word:
#             if i not in node.child:
#                 return False
#             node = node.child[i]
#         return node.is_end
#
#     def prefix_search(self,word):
#         node = self.root
#         for i in word:
#             if i not in node.child:
#                 return []
#             node = node.child[i]
#         return self.prefix_helper(node,word)
#
#     def prefix_helper(self,node,word):
#         res = []
#         if node.is_end:
#             res.append(word)
#
#         for char, child_node in node.child.items():
#             res.extend(self.prefix_helper(child_node,word+char))
#         return res
#
#     def remove(self, word):
#         self.removeHelper(self.root, word, 0)
#
#     def removeHelper(self, node, word, index):
#         if index == len(word):
#             node.is_end = False
#             return
#
#         letter = word[index]
#         if letter not in node.child:
#             return
#
#         child_node = node.child[letter]
#         self.removeHelper(child_node, word, index + 1)
#
#         if not child_node.child and not child_node.is_end:
#             del child_node[letter]
#
# P = PrefixTree()
# P.insert('danish')
# P.insert('dani')
# P.insert('da')
# print(P.search('danidsh'))
# P.remove('danish')
# print(P.prefix_search('dan'))



class SuffixNode:
    def __init__(self):
        self.child = {}
        self.is_end = False

class SuffixTree:
    def __init__(self):
        self.root = SuffixNode()

    def insert(self,word):
        for i in range(len(word)):
            self.insertHelper(i,word)

    def insertHelper(self, i, word):
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
        return node.is_end

    def prefix_search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.child:
                return []
            node = node.child[char]
        return self.collect_suffixes(node, prefix)

    def collect_suffixes(self, node, prefix):
        res = []
        if node.is_end:
            res.append(prefix)

        for char, child_node in node.child.items():
            res.extend(self.collect_suffixes(child_node, prefix + char))
        return res


s = SuffixTree()
s.insert('danish')
s.insert('da')
s.insert('dani')
s.insert('daniio')
print(s.search('da'))
print(s.prefix_search('d'))