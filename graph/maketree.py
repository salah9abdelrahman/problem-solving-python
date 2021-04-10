""""
https://www.spoj.com/problems/MAKETREE/

test cases:

4 2
1 3
2 3 4

7 4
2 2 3
1 6
1 7
2 1 2

"""


def topological_sort(v):
    visited = [False] * (n + 1)
    res = []
    for i in range(1, v + 1):
        if not visited[i]:
            topological_sort_util(i, visited, res)
    return res


def topological_sort_util(v, visited, res):
    visited[v] = True
    for i in adj[v]:
        if not visited[i]:
            topological_sort_util(i, visited, res)
    res.append(v)


n, k = (int(i) for i in input().split())
adj = {key: [] for key in range(1, n + 1)}
for i in range(1, k + 1):
    _, *children = (int(i) for i in input().split())
    for j in children:
        adj.get(i).append(j)

order = topological_sort(n)
print(order)
position = 0
result = [0] * (n + 1)
# 3 1 4 2
for i in range(n - 1, -1, -1):
    student = order[i]
    result[student] = position
    position = student

# print(result)
for i in range(1, n + 1):
    print(result[i])
