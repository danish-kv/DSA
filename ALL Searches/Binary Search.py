# Implement binary search to find the index of a given element in a sorted array.
def binary(arr1, find):
    l = 0
    r = len(arr1)-1

    while l <= r:
        m = (l+r) // 2
        if arr1[m] == find:
            return m
        elif find < arr1[m]:
            r = m - 1
        else:
            l = m + 1

arr = [11, 12, 21, 23, 32, 34, 45, 56, 67, 72, 87, 90]
k = 12
p = binary(arr, k)
print(p)

































