def heapsort(lst):
    # Build the heap
    for start in range((len(lst) - 2) // 2, -1, -1):
        siftdown(lst, start, len(lst) - 1)

    # Extract elements from the heap
    for end in range(len(lst) - 1, 0, -1):
        lst[end], lst[0] = lst[0], lst[end]
        siftdown(lst, 0, end - 1)
    return lst


def siftdown(lst, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1
        if lst[root] < lst[child]:
            lst[root], lst[child] = lst[child], lst[root]
            root = child
        else:
            break


sorted_list = heapsort([5, 3, 7, 1, 4, 2])
print(sorted_list)
