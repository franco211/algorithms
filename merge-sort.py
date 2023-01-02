# Merge sort is a divide and conquer algorithm
# sorts a list by dividing it in half, sorting the two halves, and then merging the sorted halves back together.

def merge_sort(arr):
  # base case: if the input list has less than 2 elements, it is already sorted
  if len(arr) < 2:
    return arr

  # divide the list in half
  mid = len(arr) // 2
  left = arr[:mid]
  right = arr[mid:]

  # recursively sort the two halves
  left = merge_sort(left)
  right = merge_sort(right)

  # merge the sorted halves
  return merge(left, right)

def merge(left, right):
  result = []
  left_index = 0
  right_index = 0
  # repeat until one of the lists is empty
  while left_index < len(left) and right_index < len(right):
    # if the current element of the left list is smaller, append it to the result
    # and move to the next element in the left list
    if left[left_index] < right[right_index]:
      result.append(left[left_index])
      left_index += 1
    # if the current element of the right list is smaller, append it to the result
    # and move to the next element in the right list
    else:
      result.append(right[right_index])
      right_index += 1
  # append the remaining elements of the left list (if any) to the result
  result.extend(left[left_index:])
  # append the remaining elements of the right list (if any) to the result
  result.extend(right[right_index:])
  return result

# test the function
print(merge_sort([5, 2, 4, 6, 1, 3]))  # [1, 2, 3, 4, 5, 6]
