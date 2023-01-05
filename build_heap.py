def max_heapify(heap, heap_size, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < heap_size and heap[left] > heap[largest]:
        largest = left
    if right < heap_size and heap[right] > heap[largest]:
        largest = right
    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        max_heapify(heap, heap_size, largest)

def build_max_heap(heap):
        heap_size = len(heap)
        for j in range(len(heap) // 2, -1, -1): 
            # The starting number is len(heap) // 2, which is the middle of the heap.
            # The ending number is -1, which is the root node of the heap. 
            # The step size is -1, which means that the loop will decrement by 1 on each iteration
            max_heapify(heap, heap_size, j)
            heap_size = len(heap)


heap = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
build_max_heap(heap)
print(heap)  # prints [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
