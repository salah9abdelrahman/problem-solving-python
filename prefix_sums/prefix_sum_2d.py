def accumulate_prefix_sum_2d_row(arr):
    s = []
    for array in arr:
        row = [0]
        for i in range(1, len(array)):
            row.append(array[i] + row[i - 1])
        s.append(row)
    return s


def accumulate_prefix_sum_2d_column(accum_row):
    for j in range(1, len(accum_row)):
        for i in range(1, len(accum_row[j])):
            accum_row[i][j] += accum_row[i - 1][j]
    return accum_row


def sum_range(i, j, k, l, accumulated_arr):
    return accumulated_arr[k][l] - accumulated_arr[k][j - 1] - accumulated_arr[i - 1][l] + accumulated_arr[i - 1][j - 1]


if __name__ == '__main__':
    arr = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 2, 2, 4, 1],
        [0, 3, 4, 1, 5, 2],
        [0, 2, 3, 3, 2, 4],
        [0, 4, 1, 5, 4, 6],
        [0, 6, 3, 2, 1, 3]
    ]
    accumulated_row = accumulate_prefix_sum_2d_row(arr)
    accumulated_col = accumulate_prefix_sum_2d_column(accumulated_row)
    print(sum_range(2, 3, 3, 5, accumulated_col))
