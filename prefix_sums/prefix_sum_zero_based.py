def sum_range(cumulative_arr, i, j):
    if i == 0:
        return cumulative_arr[j]
    return cumulative_arr[j] - cumulative_arr[i - 1]


def generate_prefix_sum(arr):
    s = []
    for i in range(len(arr)):
        s.append(arr[i] if i == 0 else arr[i] + s[i - 1])
    return s


if __name__ == '__main__':
    arr = [2, 1, 4, 5, 3, 7]
    s = generate_prefix_sum(arr)
    print(s)
    print(sum_range(s, 0, 5))
    print(sum_range(s, 2, 4))
