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

def test_max_heapify():
    heap = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    heap_size = len(heap)
    i = 1
    max_heapify(heap, heap_size, i)
    assert heap == [16, 14, 10, 8, 7, 9, 3, 2, 4, 1], 'Test Case 1 Failed'

    heap = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    heap_size = len(heap)
    i = 0
    max_heapify(heap, heap_size, i)
    assert heap == [10, 9, 3, 4, 5, 6, 7, 8, 2, 1], 'Test Case 2 Failed'

    heap = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    heap_size = len(heap)
    i = 2
    max_heapify(heap, heap_size, i)
    assert heap == [100, 20, 90, 40, 50, 60, 70, 80, 30, 10], 'Test Case 3 Failed'

    print('All test cases pass')

test_max_heapify()