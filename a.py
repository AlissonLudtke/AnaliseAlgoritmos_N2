import time
import random

# Original algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr

# Improved algorithms
def bubble_sort_improved(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def selection_sort_improved(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort_improved(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr

# Create an array with random numbers
arr = [random.randint(1, 1000) for _ in range(1000)]

# Measure time
def measure_time(func, arr):
    start_time = time.time()
    func(arr)
    return time.time() - start_time

print("Original BubbleSort time: ", measure_time(bubble_sort, arr.copy()))
print("Original SelectionSort time: ", measure_time(selection_sort, arr.copy()))
print("Original InsertionSort time: ", measure_time(insertion_sort, arr.copy()))
print("Improved BubbleSort time: ", measure_time(bubble_sort_improved, arr.copy()))
print("Improved SelectionSort time: ", measure_time(selection_sort_improved, arr.copy()))
print("Improved InsertionSort time: ", measure_time(insertion_sort_improved, arr.copy()))
