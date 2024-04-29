class MaxHeap:
    def __init__(self):
        self.heap = []

    def heapify_up(self, index):
        parent = (index - 1) // 2

        if parent >= 0 and self.heap[index] > self.heap[parent]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.heapify_up(parent)

    def heapify_down(self, index):
        lchild = (index * 2) + 1
        rchild = (index * 2) + 2
        largest = index

        if lchild < len(self.heap) and self.heap[largest] < self.heap[lchild]:
            largest = lchild
        if rchild < len(self.heap) and self.heap[largest] < self.heap[rchild]:
            largest = rchild

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)

    def insert(self, data):
        self.heap.append(data)
        self.heapify_up(len(self.heap) - 1)

    def remove(self, data):
        index = self.heap.index(data)

        self.heap[index], self.heap[-1] = self.heap[-1], self.heap[index]

        del self.heap[-1]
        self.heapify_down(index)

    def peek_max(self):
        if self.heap:
            return self.heap[0]
        return None

    def extract_max(self):
        if self.heap:
            max = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.heapify_down(0)
            return max
        return None



h = MaxHeap()
mylist = [3,1,8,5,9,434,2,73]
for i in mylist:
    h.insert(i)

print(h.heap)
h.remove(3)
print('After Deletion')
print(h.heap)
print()
print("Top Value",h.peek_max())
print("Extract the Value from MAX HEAP :-",h.peek_max())