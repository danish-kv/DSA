# selertion sort

# arr = [12, 34, 0, 1, 7, 64, 1]


# for i in range(len(arr)):
#     min = i
#     for j in range(i+1,len(arr)):
#         if arr[j] < arr[min]:
#             min = j
#     arr[min], arr[i] = arr[i], arr[min]
#
# print(arr)


# Bubble sort
#
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[j] < arr[i]:
#             arr[i], arr[j] = arr[j], arr[i]
# print(arr)


# insertion sort

# for i in range(1, len(arr)):
#     current = arr[i]
#     j = i - 1
#     while j >= 0 and arr[j] > current:
#         arr[j + 1] = arr[j]
#         j -= 1
#
#     arr[j + 1] = current
# print(arr)


# quick sort

# def pivot_index(array, first, last):
#     pivot = array[first]
#     left = first + 1
#     right = last
#
#     while True:
#         while left <= right and array[left] <= pivot:
#             left += 1
#         while left <= right and array[right] >= pivot:
#             right -= 1
#
#         if left > right:
#             break
#         else:
#             array[left], array[right] = array[right], array[left]
#
#     array[first], array[right] = array[right], array[first]
#     return right
#
#
# def quicksort(array, first, last):
#     if  first < last:
#         p = pivot_index(array, first, last)
#         quicksort(array, first, p - 1)
#         quicksort(array, p + 1, last)
#
#     return array
# print(quicksort(arr, 0, len(arr)-1))


# Merge Sort
# def merge_sort(array):
#     if len(array) > 1:
#         mid = len(array) // 2
#         left_half = array[:mid]
#         right_half = array[mid:]
#         merge_sort(left_half)
#         merge_sort(right_half)
#         i, j, k = 0, 0, 0
#
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 array[k] = left_half[i]
#                 i += 1
#                 k += 1
#             else:
#                 array[k] = right_half[j]
#                 j += 1
#                 k += 1
#
#         while i < len(left_half):
#             array[k] = left_half[i]
#             i += 1
#             k += 1
#
#         while j < len(right_half):
#             array[k] = right_half[j]
#             j += 1
#             k += 1
#
# merge_sort(arr)
# print(arr)


def pivot_index(array, first, last):
    pivot = array[first]
    left = first + 1
    right = last

    while True:
        while left <= right and array[left] <= pivot:
            left += 1

        while left <= right and array[right] >= pivot:
            right -= 1

        if left > right:
            break
        else:
            array[left], array[right] = array[right], array[left]

    array[first], array[right] = array[right], array[first]

    return right


def quickSort(array, first, last):
    if first < last:
        p = pivot_index(array, first, last)
        quickSort(array, first, p - 1)
        quickSort(array, p + 1, last)


array = [12, 5, 8, 1, 0, 1, 76, 9]
quickSort(array,0,len(array)-1)
print(array)
