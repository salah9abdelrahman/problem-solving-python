def get_cell_num(i, j):
    return (i - 1) * m + j


n1 = input().split()
n, m, k, t = map(int, n1)
wasted = []
plants = ['Grapes', 'Carrots', 'Kiwis']

for i in range(k):
    c1, c2 = map(int, input().split())
    wasted.append(get_cell_num(c1, c2))
wasted.sort()
# print(wasted)
for i in range(t):
    n1 = input()
    c1, c2 = map(int, n1.split())
    cell_num = get_cell_num(c1, c2)
    if cell_num in wasted:
        print('Waste')
    else:
        for cell in wasted:
            if cell < cell_num:
                cell_num -= 1
            else:
                break
        print(plants[cell_num % 3])
