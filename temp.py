l = 5


def get_cell_num(i, j):
    return (i - 1) * l + j


x = get_cell_num(2, 3)
print(x)
j = x % l
print(j)
print(x // l)

x = [1, 2,3]
x.re