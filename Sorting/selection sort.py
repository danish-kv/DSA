arr = [1, 20, 2, 90, 23, 1, 5, 67, 21]

for i in range(len(arr)):
    min = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min]:
            min = j
    arr[i], arr[min] = arr[min], arr[i]

print(arr)



# Using min()
# for i in range(len(arr)):
#     min_val = min(arr[i:])
#     min_index = arr.index(min_val,i)
#     arr[i], arr[min_index] = arr[min_index], arr[i]
# print(arr)