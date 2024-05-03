arr = [64, 34, 25, 12, 22, 11, 90]

for i in range(1,len(arr)):
    current = arr[i]
    j = i - 1
    while j >= 0 and arr[j] >= current:
        arr[j+1] = arr[j]
        j -= 1

    arr[j+1] = current

print(arr)
