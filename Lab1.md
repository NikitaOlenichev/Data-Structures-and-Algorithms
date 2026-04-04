# Лабораторная работа 1
## Экспериментальное исследование сложности алгоритмов

### Выполнил Оленичев Никита Романович, группа ИДБ-25-07

### 1.Проверка наличия элемента в массиве

```python
import time
import random


def measure_time(func, data):
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return end - start

def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr

def x_in_arr(arr):
    n = 16
    for i in range(len(arr)):
        if arr[i] == n:
            return True
    return False

if __name__ == '__main__':
    sizes = [100, 1000, 5000, 10000]
    for x in sizes:
        arr = generate_array(x)
        t = measure_time(x_in_arr, arr)
        print(x, "{:5f}".format(t))
```
| n | t,с |
|---|---|
| 100 | 0.000006 |
| 1000 | 0.000073 |
| 5000 | 0.000333 |
| 10000 | 0.000350 |

### 2.Поиск второго максимального элемента

```python
import time
import random


def measure_time(func, data):
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return end - start

def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr

def second_max(arr):
    max1 = arr[0]
    max2 = arr[0]
    for i in range(len(arr)):
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2 and arr[i] != max1:
            max2 = arr[i]
    return max2

if __name__ == '__main__':
    sizes = [100, 1000, 5000, 10000]
    for x in sizes:
        arr = generate_array(x)
        t = measure_time(second_max, arr)
        print(x, "{:5f}".format(t))
```
| n | t,с |
|---|---|
| 100 | 0.000010 |
| 1000 | 0.000055 |
| 5000 | 0.000295 |
| 10000 | 0.000631 |

### 3. Бинарный поиск

```python
import time
import random


def measure_time(func, data):
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return end - start

def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr

def bin_search(arr):
    arr = sorted(arr)
    target = 27
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == '__main__':
    sizes = [100, 1000, 5000, 10000]
    for x in sizes:
        arr = generate_array(x)
        t = measure_time(bin_search, arr)
        print(x, "{:5f}".format(t))
```
| n | t,с |
|---|---|
| 100 | 0.000017 |
| 1000 | 0.000135 |
| 5000 | 0.000744 |
| 10000 | 0.001640 |

### 4. Построение таблицы умножения

```python
import time
import random


def measure_time(func, data):
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return end - start

def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr

def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i * j, end='\t')
        print()

if __name__ == '__main__':
    sizes = [3, 7, 10, 100]
    for x in sizes:
        t = measure_time(multiplication_table, x)
        print(x, "{:5f}".format(t))
```
| n | t,с |
|---|---|
| 3 | 0.000061 |
| 7 | 0.000143 |
| 10 | 0.000304 |
| 100 | 0.108473 |

## Замеры алгоритмической и пространственной сложности любой из сортировок

Сортировка слиянием:

```python
import time
import random
import tracemalloc

def measure_time(func, data):
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return end - start

def measure_memory(func, data):
    tracemalloc.start()
    func(data)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak

def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)
    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    return merge(left_list, right_list)

if __name__ == '__main__':
    sizes = [100, 1000, 5000, 10000]
    for x in sizes:
        arr = generate_array(x)
        t = measure_time(merge_sort, arr)
        m = measure_memory(merge_sort, arr)
        print(x, "{:5f}".format(t), "{:5f}".format(m / 1024 / 1024))
```
| n | t,с | m,мегабайт |
|---|---|---|
| 100 | 0.000138 | 0.001747 |
| 1000 | 0.002113 | 0.016563 |
| 5000 | 0.010467 | 0.080116 |
| 10000 | 0.022392 | 0.161186 |
