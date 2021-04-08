"""
https://www.spoj.com/problems/TOPOSORT/

used algorithm: Khan's algorithm
"""
from collections import deque


def find_top_ordering():
    adj_len = len(adj)
    in_degree = [0 for _ in range(adj_len)]
    # cal in degree
    for i in range(adj_len):
        for j in adj[i]:
            in_degree[j] = in_degree[j] + 1
    # print(in_degree)
    q = deque()
    for i in range(len(adj)):
        if in_degree[i] == 0:
            q.append(i)

    index = 0
    order = [0 for _ in range(adj_len)]
    while q:
        node = q.popleft()
        order[index] = node
        index = index + 1
        for i in adj[node]:
            in_degree[i] = in_degree[i] - 1
            if in_degree[i] == 0:
                q.append(i)

    if index != n:
        return "Sandro fails."
    else:
        return [i + 1 for i in order]


n, d = (int(i) for i in input().split())

adj = {key: [] for key in range(n)}

for i in range(d):
    v, e = (int(i) - 1 for i in input().split())
    adj.get(v).append(e)

print(find_top_ordering())

"""
8 9
1 4
1 2
4 2
4 3
3 2
5 2
3 5
8 2
8 6

2 2
1 2
2 1

6 4
5 1
1 2
2 3
4 6
"""
