import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def bucket_sort(arr):
    bucket_size = 10
    if len(arr) == 0:
        return arr

    min_val, max_val = min(arr), max(arr)
    num_buckets = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(num_buckets)]

    for num in arr:
        idx = (num - min_val) // bucket_size
        buckets[idx].append(num)

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr

def generate_random_array(size, data_type):
    if data_type == 'int':
        return [random.randint(1, 1000) for _ in range(size)]
    elif data_type == 'float':
        return [random.uniform(1, 1000) for _ in range(size)]
    elif data_type == 'string':
        return ["".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=random.randint(1, 10))) for _ in range(size)]

def test_algorithm(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": lambda arr: quick_sort(arr, 0, len(arr) - 1),
        "Insertion Sort": insertion_sort,
        "Selection Sort": selection_sort,
        "Bucket Sort": bucket_sort
    }

    input_size = int(input("Enter the size of the array: "))
    data_type = input("Enter the data type (int, float, string): ")

    arr = generate_random_array(input_size, data_type)

    print("\nTesting sorting algorithms:")
    for name, func in algorithms.items():
        arr_copy = arr[:]
        exec_time = test_algorithm(func, arr_copy)
        print(f"{name}: {exec_time:.6f} seconds")
