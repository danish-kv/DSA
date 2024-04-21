class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key,value)]
        else:
            self.table[index].append((key,value))

    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return print(v)
        return None

    def remove(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for i, (k,_) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    return
        print('KEy not found')

    def print(self):
        for i in range(self.size):
            print(f"Bucket {i}: {self.table[i]}")


hashh = HashTable(5)
hashh.insert(23, 23)
hashh.insert(23, 2223)
hashh.remove(23)
hashh.print()



