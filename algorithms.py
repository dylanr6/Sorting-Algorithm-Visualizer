def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                yield array, j, j+1

def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if array[j] < array[min_idx]:
                min_idx = j
            # Pause after each comparison so to enable highlighting the bars
            yield array, i, j
        if min_idx != i:
            array[i], array[min_idx] = array[min_idx], array[i]
            # Pause after the swap
            yield array, i, min_idx
