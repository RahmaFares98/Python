def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


example_list = [64, 25, 12, 22, 11,6,7,36,23,3]
sorted_list = selection_sort(example_list)
print("Sorted list:", sorted_list)
