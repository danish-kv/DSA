# # Bubble sort
# arr = [23,6,1,98,5,1,0]
# # for i in range(len(arr)):
# #     for j in range(i+1,len(arr)):
# #         if arr[i] > arr[j]:
# #             arr[i], arr[j] = arr[j], arr[i]
# #
# # print(arr)
#
#
# # Insertion Sort
#
# # for i in range(1,len(arr)):
# #     current = arr[i]
# #     j = i-1
# #     while j >= 0 and arr[j] > current:
# #         arr[j+1] = arr[j]
# #         j -= 1
# #     arr[j+1] = current
# # print(arr)
#
#
# # Selection sort
#
# for i in range(len(arr)):
#     min = i
#     for j in range(i+1,len(arr)):
#         if arr[j] < arr[min]:
#             min = j
#
#     arr[i], arr[min] = arr[min], arr[i]
#
# print(arr)
#
#
# # Quick Sort
# def pivot_index(arr,first, last):
#     pivot = arr[first]
#     left = first + 1
#     right = last
#     while True:
#         while left <= right and arr[left] <= pivot:
#             left += 1
#         while left <= right and arr[right] >= pivot:
#             right -= 1
#         if left >= right:
#             break
#         else:
#             arr[left],arr[right] = arr[right], arr[left]
#     arr[first], arr[right] = arr[right], arr[first]
#     return right
#
# def quicksort(arr,first, last):
#     if first < last:
#         p = pivot_index(arr,first,last)
#         quicksort(arr,first,p-1)
#         quicksort(arr,p+1,last)
#
# quicksort(arr,0,len(arr)-1)
# print(arr)
#
#
#
#
# def mergesort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]
#         mergesort(left_half)
#         mergesort(right_half)
#         i, j, k = 0, 0, 0
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k]  = left_half[i]
#                 i += 1
#                 k += 1
#             else :
#                 arr[k] = right_half[j]
#                 j += 1
#                 k += 1
#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1
#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1
#
# mergesort(arr)
# print(arr)
#
#
# for i in range(len(arr)):
#     min = i
#     for i in range(i+1,len(arr)):
#         if arr[j] >  arr[min]:
#             min = j
#
#     arr[i], arr[min] = arr[min], arr[i]
#
# print(arr)




# Hash table using number
# class HashTable:
#     def __init__(self, size):
#         self.size = size
#         self.item = [None] * size
#
#     def hash_function(self,key):
#         return key % self.size
#
#     def insert(self,key,value):
#         index = (self.hash_function(key))
#         if self.item[index] is None:
#             self.item[index] = [(key,value)]
#         else:
#             self.item[index].append((key,value))
#
#     def search(self,key):
#         index = self.hash_function(key)
#         if self.item[index] is not None:
#             for k, v in self.item[index]:
#                 if k == key:
#                     return v
#         return None
#
#     def delete(self,key):
#         index = self.hash_function(key)
#         if self.item[index] is not None:
#             for i, (k, _) in enumerate(self.item[index]):
#                 if key == k:
#                     del self.item[index][i]
#                     return
#         print('Key not found')
#
#
#     def display(self):
#         for i in range(self.size):
#             print(i,' : ', self.item[i])
#         # return print(self.item)
#
#
# HT = HashTable(10)
# HT.insert(10,100)
# HT.insert(100,10)
# HT.insert(1,2)
# HT.insert(22,33)
#
# HT.display()




# HashTable using string

class HashTable:
    def __init__(self, size):
        self.size = size
        self.item = [None] * size

    def hash_function(self,key):
        code = 0
        for i in str(key):
            code += ord(i)
        return code % self.size

    def insert(self,key,value):
        index = (self.hash_function(key))
        if self.item[index] is None:
            self.item[index] = [(key,value)]
        else:
            self.item[index].append((key,value))

    def search(self,key):
        index = self.hash_function(key)
        if self.item[index] is not None:
            for k, v in self.item[index]:
                if k == key:
                    return print(v)
        return None

    def delete(self,key):
        index = self.hash_function(key)
        if self.item[index] is not None:
            for i, (k, _) in enumerate(self.item[index]):
                if key == k:
                    del self.item[index][i]
                    return
        print('Key not found')


    def display(self):
        for i in range(self.size):
            print(i,' : ', self.item[i])
        # return print(self.item)

HT = HashTable(10)
HT.insert('muhammed','danish')
HT.search('muhammed')
HT.display()