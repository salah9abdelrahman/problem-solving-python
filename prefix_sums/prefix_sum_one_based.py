def sum_range(cumulative_arr, i, j):
    return cumulative_arr[j] - cumulative_arr[i - 1]


def generate_prefix_sum(arr):
    s = [0]
    for i in range(1, len(arr)):
        s.append(arr[i] + s[i - 1])
    return s


if __name__ == '_ _main__':
    arr = [0, 2, 1, 4, 5, 3, 7]
    s = generate_prefix_sum(arr)
    print(s)

    # one based queries
    print(sum_range(s, 1, 6))
    print(sum_range(s, 3, 5))
