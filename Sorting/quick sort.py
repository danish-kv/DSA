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


def quicksort(array, first, last):
    if first < last:
        p = pivot_index(array, first, last)
        quicksort(array, first, p - 1)
        quicksort(array, p + 1, last)


array = [20, 11, 2, 5, 9]
print(array)
quicksort(array, 0, len(array) - 1)
print(array)
