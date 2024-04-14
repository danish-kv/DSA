# Write a Python program to reverse an array in-place.
# def rev_array(arr):
#     arr[:] = arr[::-1]
#
# array = [1, 2, 3, 4, 5]
# rev_array(array)
# print(array)


# Implement a function to find the second largest element in an array.
def second_largest(arr):
    lar = 0
    sec = 0
    for i in arr:
        if i > lar:
            sec = lar
            lar = i
        elif i > sec and i != sec:
            sec = i

    return sec

print(second_largest([1,2,10,3,4,5]))


# Write a program to merge two sorted arrays into a single sorted array.

def merge_sorted_array(arr1,arr2):
    merge = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merge.append(arr1[i])
            i += 1
        else:
            merge.append(arr2[j])
            j += 1

    while i < len(arr1):
        merge.append(arr1[i])
        i += 1

        # Append the remaining elements from arr2, if any
    while j < len(arr2):
        merge.append(arr2[j])
        j += 1

    return merge

print(merge_sorted_array([1,2,4,5], [12,23,34,45]))


