def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
elements = [39, 12, 18, 85, 72, 10, 2, 18]
print("Unsorted list is:")
print(elements)
selection_sort(elements)
print("Sorted list is:")
print(elements)
