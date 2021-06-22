"""
1 3 4 5 9 9 9 12 15
"""

# find the first 9
arr = [1, 3, 4, 5, 9, 9, 9, 12, 15]


def binary_search_first(start, end, value):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < value:
            start = mid + 1
        elif arr[mid] > value:
            end = mid - 1
        else:
            end = mid
    return start


def binary_search_last(start, end, value):
    while start < end:
        # mid = (start + end) // 2
        mid = start + (end - start) // 2
        if arr[mid] < value:
            start = mid + 1
        elif arr[mid] > value:
            end = mid - 1
        else:
            start = mid
    return start


if __name__ == '__main__':
    print(binary_search_first(0, len(arr), 9))
    print(binary_search_last(0, len(arr), 9))
