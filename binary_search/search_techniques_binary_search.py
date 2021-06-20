"""
1 3 4 5 9 9 9 12 15
"""

# find the first 9
arr = [1, 3, 4, 5, 9, 9, 9, 12, 15]


def BS_first(start,  end,  value):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < value:
            start = mid + 1
        elif arr[mid] > value:
            end = mid - 1
        else:
            end = mid
    return start


# start = 1, end = 2
#mid = 1
def BS_last(start,  end,  value):
    while start < end:
        # mid = (start + end) // 2
        mid = start + (end - start) // 2
        if arr[mid] <= value:
            start = mid + 1
        elif arr[mid] > value:
            end = mid - 1
        else:
            start = mid
    return start


if __name__ == '__main__':
    print(BS_first(0, len(arr), 9))
    print(BS_last(0, len(arr), 9))
