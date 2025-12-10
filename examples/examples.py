from typing import List, Optional, Tuple
import random

# O(1) - constant time
# Returns the first element or None if empty.
def get_first_element(arr: List[int]) -> Optional[int]:
    if arr:
        return arr[0]
    return None

# O(log n) - binary search on a sorted list
# Returns index of target or -1 if not found.
def binary_search(sorted_arr: List[int], target: int) -> int:
    lo, hi = 0, len(sorted_arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_arr[mid] == target:
            return mid
        if sorted_arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# O(n) - linear time
# Sum all elements.
def linear_sum(arr: List[int]) -> int:
    total = 0
    for x in arr:
        total += x
    return total

# O(n) - linear time
# Linear search for target; returns index or -1.
def linear_search(arr: List[int], target: int) -> int:
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1

# O(n^2) - quadratic time (brute force)
# Return first pair of indices whose values sum to target, or None.
def find_pair_with_sum_bruteforce(arr: List[int], target: int) -> Optional[Tuple[int, int]]:
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return (i, j)
    return None

# O(n^2) - bubble sort (in-place on a copy)
# Returns a sorted copy of the input list.
def bubble_sort(arr: List[int]) -> List[int]:
    a = arr.copy()
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a

# O(log n) - repeated halving
# Counts how many times n can be halved until zero.
def repeated_halving(n: int) -> int:
    count = 0
    while n > 0:
        n //= 2
        count += 1
    return count

# O(n^3) - cubic time (for reference)
# Triple nested loops example; grows very quickly.
def triple_nested_sum(arr: List[int]) -> int:
    total = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                total += arr[i] + arr[j] + arr[k]
    return total

# Utility to demonstrate calls (does not need to be executed)
def example_run():
    a = [random.randint(0, 100) for _ in range(12)]
    print("array:", a)
    print("get_first_element:", get_first_element(a))
    print("linear_sum:", linear_sum(a))
    print("linear_search(50):", linear_search(a, 50))
    print("bubble_sort:", bubble_sort(a))
    print("merge_sort:", merge_sort(a))
    sorted_a = sorted(a)
    print("sorted array:", sorted_a)
    print("binary_search(sorted, value):", binary_search(sorted_a, sorted_a[0]) if sorted_a else -1)
    print("find_pair_with_sum_bruteforce(100):", find_pair_with_sum_bruteforce(a, 100))
    print("repeated_halving(1000):", repeated_halving(1000))
    small = [1, 2, 3]
    print("triple_nested_sum(small):", triple_nested_sum(small))

# Analyze the functions using the big_o library (if available).
# This function is only defined and not executed automatically.
def analyze_with_big_o():
    try:
        import big_o
    except Exception:
        print("big_o not available. Install with: pip install big_o")
        return

    # wrappers that accept a single integer n for the big_o generator
    def get_first_element_n(n: int):
        arr = list(range(n))
        return get_first_element(arr)

    def linear_sum_n(n: int):
        arr = list(range(n))
        return linear_sum(arr)

    def linear_search_n(n: int):
        arr = list(range(n))
        return linear_search(arr, n - 1)

    def binary_search_n(n: int):
        arr = list(range(n))
        return binary_search(arr, n - 1)

    def find_pair_with_sum_bruteforce_n(n: int):
        # small values recommended for O(n^2) analysis
        arr = list(range(n))
        return find_pair_with_sum_bruteforce(arr, n - 1)

    def bubble_sort_n(n: int):
        # worst-case: reverse-sorted list
        arr = list(range(n, 0, -1))
        return bubble_sort(arr)

    def merge_sort_n(n: int):
        arr = list(range(n, 0, -1))
        return merge_sort(arr)

    def repeated_halving_n(n: int):
        return repeated_halving(n)

    def triple_nested_sum_n(n: int):
        # keep small n to avoid excessive runtime
        arr = list(range(max(0, min(n, 15))))
        return triple_nested_sum(arr)

    tests = [
        ("get_first_element", get_first_element_n, dict(min_n=1, max_n=1000)),
        ("linear_sum", linear_sum_n, dict(min_n=10, max_n=2000)),
        ("linear_search", linear_search_n, dict(min_n=10, max_n=2000)),
        ("binary_search", binary_search_n, dict(min_n=10, max_n=200000)),
        ("find_pair_with_sum_bruteforce", find_pair_with_sum_bruteforce_n, dict(min_n=10, max_n=300)),
        ("bubble_sort", bubble_sort_n, dict(min_n=10, max_n=2000)),
        ("merge_sort", merge_sort_n, dict(min_n=10, max_n=20000)),
        ("repeated_halving", repeated_halving_n, dict(min_n=10, max_n=1000000)),
        ("triple_nested_sum", triple_nested_sum_n, dict(min_n=1, max_n=15, n_measures=5)),
    ]

    for name, func, params in tests:
        try:
            # use big_o.datagen.n_ which provides integer n to the wrapper
            generator = big_o.datagen.n_
            # merge default parameters; some tests reduce measures for heavy ops
            args = dict(generator=generator, n_repeats=3)
            args.update(params)
            result = big_o.big_o(func, **args)
            print(f"{name}: {result}")
        except Exception as e:
            print(f"{name}: analysis failed ({e})")

# no automatic execution on import