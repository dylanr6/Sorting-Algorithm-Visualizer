#Bubble Sort Function
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                yield array, j, j+1

#Selection Sort Function
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


#Merge Sort Functions
def merge(arr, left, mid, right):
    merged = []
    i, j = left, mid + 1

    #Merge two already-sorted halves
    while i <= mid and j <= right:
        yield arr, i, j

        if arr[i] < arr[j]:
            merged.append(arr[i])
            i += 1
        else:
            merged.append(arr[j])
            j += 1

    #Add the remainders
    while i <= mid:
        yield arr, i, i
        merged.append(arr[i])
        i += 1

    while j <= right:
        yield arr, j, j
        merged.append(arr[j])
        j += 1

    #Copy the now merged list back to an array
    for k, val in enumerate(merged):
        arr[left + k] = val
        yield arr, left + k, left + k

def merge_sort(arr, left, right):
    if right - left <= 0:
        return
    mid = (left + right) // 2

    #Sorts the left halve
    yield from merge_sort(arr, left, mid)

    #Sorts the right halve
    yield from merge_sort(arr, mid + 1, right)

    #Merge the halves
    yield from merge(arr, left, mid, right)