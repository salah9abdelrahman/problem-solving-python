"""https://codeforces.com/contest/129/problem/B"""


def init_graph(n1, n2):
    if adj.get(n1) is not None:
        adj[n1].append(n2)
    else:
        adj[n1] = [n2]


n, m = map(int, input().split())
adj = {}
edges = [0 for i in range(n)]
edges.insert(0, 0)
for i in range(m):
    n1, n2 = map(int, input().split())
    init_graph(n1, n2)
    init_graph(n2, n1)
    edges[n1] += 1
    edges[n2] += 1

sol = 0
removed = []
while True:
    for edge in range(1, len(edges)):
        if edges[edge] == 1 and adj.get(edge):
            edges[edge] = 0
            # append the relation to reduce  the edge later
            removed.append(adj[edge][0])
            # remove the relation from the current node and the related edge
            adj[adj[edge][0]].remove(edge)
            adj.pop(edge)

    for i in removed:
        edges[i] -= 1

    if len(removed) == 0 or len(adj) == 0:
        break

    else:
        sol += 1
        removed = []

print(sol)
