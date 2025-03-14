import random
import time
import matplotlib.pyplot as plt

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    arr[0], arr[pivot_index] = arr[pivot_index], arr[0] 
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return randomized_quick_sort(left) + [pivot] + randomized_quick_sort(right)


def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return deterministic_quick_sort(left) + [pivot] + deterministic_quick_sort(right)


def measure_time(sorting_function, arr):
    start_time = time.time()
    sorting_function(arr)
    return time.time() - start_time

def test_algorithms():
    sizes = [10000, 50000, 100000, 500000]
    results = []
    
    for size in sizes:
        arr = [random.randint(1, 1000000) for _ in range(size)]
        
        randomized_times = []
        for _ in range(5):
            arr_copy = arr.copy()
            randomized_times.append(measure_time(randomized_quick_sort, arr_copy))
        
        deterministic_times = []
        for _ in range(5):
            arr_copy = arr.copy()
            deterministic_times.append(measure_time(deterministic_quick_sort, arr_copy))
        
        results.append({
            'size': size,
            'randomized_avg': sum(randomized_times) / len(randomized_times),
            'deterministic_avg': sum(deterministic_times) / len(deterministic_times)
        })
    
    return results




def plot_results(results):
    sizes = [result['size'] for result in results]
    randomized_times = [result['randomized_avg'] for result in results]
    deterministic_times = [result['deterministic_avg'] for result in results]
    
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, randomized_times, label='Randomized QuickSort', marker='o')
    plt.plot(sizes, deterministic_times, label='Deterministic QuickSort', marker='o')
    
    plt.xlabel('Array Size')
    plt.ylabel('Average Time (seconds)')
    plt.title('Performance Comparison of Randomized and Deterministic QuickSort')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    results = test_algorithms()
    for result in results:
        print(f"Size: {result['size']} - Randomized QuickSort: {result['randomized_avg']:.6f} seconds, "
              f"Deterministic QuickSort: {result['deterministic_avg']:.6f} seconds")
    
    plot_results(results)
