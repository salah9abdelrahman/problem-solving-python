"""
https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1552

4
1 4 5 7
4
4 6 8 10


"""

n = int(input())
heights_of_ladies = [int(i) for i in input().split()]
q = int(input())
heights_of_luchu = [int(i) for i in input().split()]


def binary_serach_up(start, end, value):
    while start <= end:
        mid = (start + end) // 2
        if heights_of_ladies[mid] <= value:
            start = mid + 1
        else:
            end = mid - 1
    if start >= len(heights_of_ladies):
        return "X"
    return heights_of_ladies[start]


def binary_serach_down(start, end, value):
    while start <= end:
        mid = (start + end) // 2
        if heights_of_ladies[mid] < value:
            start = mid + 1
        else:
            end = mid - 1
    if end < 0:
        return "X"
    return heights_of_ladies[end]


for i in range(q):
    value = heights_of_luchu[i]
    start = 0
    end = n
    if value > heights_of_ladies[-1]:
        print(heights_of_ladies[-1], 'X')
    elif value < heights_of_ladies[0]:
        print('X', heights_of_ladies[0])
    else:
        first, second = binary_serach_down(0, len(
            heights_of_ladies) - 1, value), binary_serach_up(0, len(heights_of_ladies) - 1, value)
        print(first, second)
