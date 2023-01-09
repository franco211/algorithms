
def maximum_heap(heap, heap_size):
    if heap_size < 1:
        return None
    max = heap[1]
    heap[1] = heap[-1]
    heap_size -= 1
    #siftdown(heap, 1, heap_size - 1)2    return max

heap = [2, 7, 6, 9, 3]
heap_size = 5
max = maximum_heap(heap, heap_size)
print(max)  # prints 9
print(heap)  # prints [None, 7, 3, 6, 2]