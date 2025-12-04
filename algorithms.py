#Bubble Sort Function
def bubble_sort(array):
    comparisons = 0
    swaps = 0
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swaps += 1
                yield array, j, j+1, comparisons, swaps


#Selection Sort Function
def selection_sort(array):
    comparisons = 0
    swaps = 0
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comparisons += 1
            if array[j] < array[min_idx]:
                min_idx = j
            # Pause after each comparison so to enable highlighting the bars
            yield array, i, j, comparisons, swaps
        if min_idx != i:
            array[i], array[min_idx] = array[min_idx], array[i]
            swaps += 1
            # Pause after the swap
            yield array, i, min_idx, comparisons, swaps


#Merge Sort Functions
def merge(arr, left, mid, right, comparisons=0, swaps=0):
    merged = []
    i, j = left, mid + 1

    #Merge two already-sorted halves
    while i <= mid and j <= right:
        comparisons += 1
        yield arr, i, j, comparisons, swaps

        if arr[i] < arr[j]:
            merged.append(arr[i])
            i += 1
        else:
            merged.append(arr[j])
            j += 1

    #Add the remainders
    while i <= mid:
        yield arr, i, i, comparisons, swaps
        merged.append(arr[i])
        i += 1

    while j <= right:
        yield arr, j, j, comparisons, swaps
        merged.append(arr[j])
        j += 1

    #Copy the now merged list back to an array
    for k, val in enumerate(merged):
        arr[left + k] = val
        swaps += 1
        yield arr, left + k, left + k, comparisons, swaps

def merge_sort(arr, left, right, comparisons=0, swaps=0):
    if right - left <= 0:
        return
    mid = (left + right) // 2

    #Sorts the left halve
    yield from merge_sort(arr, left, mid, comparisons, swaps)

    #Sorts the right halve
    yield from merge_sort(arr, mid + 1, right, comparisons, swaps)

    #Merge the halves
    yield from merge(arr, left, mid, right, comparisons, swaps)


#Quick Sort Functions
def partition(arr, low, high, comparisons, swaps):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        comparisons += 1
        yield arr, j, high, comparisons, swaps  #highlights the pivot and current selected element

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1
            yield arr, i, j, comparisons, swaps
    
    #Moves the pivot to the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    swaps += 1
    yield arr, i + 1, high, comparisons, swaps

    return i + 1, comparisons, swaps

def quick_sort(arr, low, high, comparisons=0, swaps=0):
    if low < high:
        pivot_index, comparisons, swaps = yield from partition(arr, low, high, comparisons, swaps)
        yield from quick_sort(arr, low, pivot_index - 1, comparisons, swaps)
        yield from quick_sort(arr, pivot_index + 1, high, comparisons, swaps)