# Selection sort is an in-place comparison sorting algorithm that works by dividing the input list into two parts: 
# a sorted sublist of items that are already in the correct order, and a sublist of the remaining unsorted items. 
# At each step in the algorithm, the next smallest element is selected from the unsorted sublist and is appended to the end of the sorted sublist.

def selection_sort(arr):
  # loop through the list
  for i in range(len(arr)):
    # find the minimum element in the unsorted sublist
    min_index = i
    for j in range(i+1, len(arr)):
      if arr[min_index] > arr[j]:
        min_index = j
    # swap the minimum element with the first element of the unsorted sublist
    arr[i], arr[min_index] = arr[min_index], arr[i]
  return arr

# test the function
print(selection_sort([5, 2, 4, 6, 1, 3]))  # [1, 2, 3, 4, 5, 6]
