def linear_search(n, key):
    for i in n:
        if key == i:
            return n.index(i)


nums = [10, 20, 30, 40, 50]
target = 20
p = linear_search(nums, target)
print(p)


# Write a program to search for a specific word in a list of words using linear search.
def string_search(string, find):
    for i in range(len(string)):
        if find == string[i]:
            return i


# Create a function to find the maximum element in an array using linear search.
def find_max(arr):
    lar = arr[0]
    for i in arr:
        if i > lar:
            lar = i
    return lar


print(find_max([10, 20, 30, 40, 50]))
