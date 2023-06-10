from bisect import bisect_right
import time
import random
import matplotlib.pyplot as plt # pip install matplotlib


# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Selection Sort


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Insertion Sort


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Improved Bubble Sort


def improved_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Improved Selection Sort


def improved_selection_sort(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        min_idx = left
        max_idx = right
        for i in range(left, right+1):
            if arr[i] < arr[min_idx]:
                min_idx = i
            if arr[i] > arr[max_idx]:
                max_idx = i
        arr[left], arr[min_idx] = arr[min_idx], arr[left]
        if max_idx == left:
            max_idx = min_idx
        arr[right], arr[max_idx] = arr[max_idx], arr[right]
        left += 1
        right -= 1
    return arr

# Improved Insertion Sort


def improved_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        pos = bisect_right(arr, key, 0, i)
        arr = arr[:pos] + [key] + arr[pos:i] + arr[i+1:]
    return arr

def measure_time(sort_function, arr):
    start = time.time()
    sort_function(arr)
    end = time.time()
    return end - start

# def plot_times(sort_functions, labels, sizes):
#     for sort_function, label in zip(sort_functions, labels):
#         times = []
#         for size in sizes:
#             arr = random.sample(range(size), size)
#             time = measure_time(sort_function, arr)
#             times.append(time)
#         plt.plot(sizes, times, label=label)
#     plt.xlabel('Size of list')
#     plt.ylabel('Time to sort (s)')
#     plt.legend()
#     plt.show()


# sort_functions = [bubble_sort, selection_sort, insertion_sort,
#                   improved_bubble_sort, improved_selection_sort, improved_insertion_sort]
# labels = ['Bubble Sort', 'Selection Sort', 'Insertion Sort',
#           'Improved Bubble Sort', 'Improved Selection Sort', 'Improved Insertion Sort']
# sizes = [1000, 5000, 10000, 15000, 20000]

# plot_times(sort_functions, labels, sizes)


arr = [random.randint(1, 1000) for _ in range(1000000)]

print("Original BubbleSort time: ", measure_time(bubble_sort, arr.copy()))
print("Original SelectionSort time: ", measure_time(selection_sort, arr.copy()))
print("Original InsertionSort time: ", measure_time(insertion_sort, arr.copy()))
print("Improved BubbleSort time: ", measure_time(improved_bubble_sort, arr.copy()))
print("Improved SelectionSort time: ", measure_time(improved_selection_sort, arr.copy()))
print("Improved InsertionSort time: ", measure_time(improved_insertion_sort, arr.copy()))
