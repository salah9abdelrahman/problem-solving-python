"""
http://codeforces.com/contest/6/problem/B
"""
n1 = input().split()
n, m = int(n1[0]), int(n1[1])
c = n1[2]
c_indexes = []
colors_set = set()
moves = [(1, 0), (0, -1), (-1, 0), (0, 1)]
desks = []


def valid_index(t):
    return 0 <= t[0] < n and 0 <= t[1] < m


for i in range(n):
    row = input()
    desks.append(row)
    for j in range(len(row)):
        if row[j] == c:
            c_indexes.append([i, j])

for i in c_indexes:
    for j in moves:
        check_indexes = i[0] + j[0], i[1] + j[1]
        if valid_index(check_indexes):
            current = desks[check_indexes[0]][check_indexes[1]]
            if current != '.' and current != c:
                colors_set.add(current)

print(len(colors_set))
