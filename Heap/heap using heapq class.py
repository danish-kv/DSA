""" Heap using heapq class """
import heapq

heap = [12, 5, 98, 2, 90, 1, 77]



""" Used For adding element  , give argument for which list """
heapq.heappush(heap, 10)



""" Used For removing element. it extract loweest node (extract root node), give argument for which list """
heapq.heappop(heap)
print(heap)



""" Used For heapify list (setting as binary heap), give argument for which list """
heapq.heapify(heap)
print(heap)
"""
    Before heapify [5, 2, 98, 10, 90, 1, 77]
    After heapify [1, 2, 5, 10, 90, 98, 77]
"""



"""Used For adding element and removing element at same time. 
and also return extracted lowest node (extract root node), give argument for which list and element"""
heapq.heappushpop(heap, 96)
print(heap)


"""Used For replacing element with root node, give argument for which list and element to replace with root node"""
heapq.heapreplace(heap,100)
print(heap)


""" Used for getting smallest element, 1st argument is how many number of element return. 2nd argument is which list"""
s = heapq.nsmallest(2,heap)
print(s)


""" Used for getting largest element, 1st argument is how many number of element return. 2nd argument is which list"""
l = heapq.nlargest(3,heap)
print(l)



priority_queue = [(1,'danish'), (4,'shadhil'), (2,'said'), (3,'mazin')]
heapq.heapify(priority_queue)
for i in range(len(priority_queue)):
    print(heapq.heappop(priority_queue))

"""
Output 
(1, 'danish')
(2, 'said')
(3, 'mazin')
(4, 'shadhil')
"""