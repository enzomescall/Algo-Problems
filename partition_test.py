import random

def find_median(arr):
    if not arr:
        return None

    n = len(arr)
    target_index1 = n // 2  # Index of the first middle element for even-length arrays
    target_index2 = target_index1 - 1  # Index of the second middle element for even-length arrays

    return (randomized_select(arr, 0, n - 1, target_index1) + randomized_select(arr, 0, n - 1, target_index2)) / 2

def randomized_select(arr, start, end, target_index):
    if start == end:
        return arr[start]

    pivot_index = randomized_partition(arr, start, end)
    
    if target_index == pivot_index:
        return arr[pivot_index]
    elif target_index < pivot_index:
        return randomized_select(arr, start, pivot_index - 1, target_index)
    else:
        return randomized_select(arr, pivot_index + 1, end, target_index)

def randomized_partition(arr, start, end):
    pivot_index = random.randint(start, end)
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]

    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

# Example usage:
array_odd = [3, 1, 4, 2, 5]
median_odd = find_median(array_odd)
print("Median (Odd):", median_odd)

array_even = [3, 1, 4, 2]
median_even = find_median(array_even)
print("Median (Even):", median_even)
