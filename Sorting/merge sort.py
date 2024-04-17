
def mergesort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]
        mergesort(left_half)
        mergesort(right_half)
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
                k += 1
            else:
                array[k] = right_half[j]
                j += 1
                k += 1
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1


array = [22,65,1,8,55,0,8]
print(array)
mergesort(array)
print(array)



