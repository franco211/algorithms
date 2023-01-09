def max_heapify(heap, heap_size, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left <= heap_size and heap[left] > heap[largest]:
        largest = left
    if right < heap_size and heap[right] > heap[largest]:
        largest = right
    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        max_heapify(heap, heap_size, largest)
