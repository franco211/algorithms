def insert_sort(arr):
    for i in range(0, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j+1] = key

arr = [5, 3, 7, 6, 9]
insert_sort(arr)
print(arr)