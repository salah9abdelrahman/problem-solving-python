"""
http://codeforces.com/contest/433/problem/B
"""


def get_prefix_arr(array):
    prefix_arr = []
    for i in range(len(array)):
        prefix_arr.append(array[i] if i == 0 else array[i] + prefix_arr[i - 1])
    return prefix_arr


def sum_range(pre_arr, i, j):
    if i == 0:
        return pre_arr[j]
    return pre_arr[j] - pre_arr[i - 1]


if __name__ == '__main__':
    n = int(input())
    s = input()
    arr = [int(i) for i in s.split()]
    arr_sorted = sorted(arr)

    arr = get_prefix_arr(arr)
    arr_sorted = get_prefix_arr(arr_sorted)
    q = int(input())
    for i in range(q):
        s = input().split()
        query = [int(i) for i in s]
        t = query[0]
        l, r = query[1] - 1, query[2] - 1
        if t == 1:
            print(sum_range(arr, l, r))
        else:
            print(sum_range(arr_sorted, l, r))
