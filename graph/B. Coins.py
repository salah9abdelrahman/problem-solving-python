"""
https://codeforces.com/contest/47/problem/B
"""
adj = {"A": [], "B": [], "C": []}

for _ in range(3):
    measure = input()
    bigger, sign, smaller = [i for i in measure]
    if sign == '<':
        bigger, smaller = smaller, bigger
    adj[smaller].append(bigger)


def topological_sort_util(graph, current_node, visited, stack):
    visited.append(current_node)

    for i in graph[current_node]:
        if i not in visited:
            topological_sort_util(graph, i, visited, stack)

    stack.insert(0, current_node)


def topological_sort(graph):
    visited = []
    stack = []

    for currentNode in graph:
        if currentNode not in visited:
            topological_sort_util(graph, currentNode, visited, stack)

    return stack


# check if it is cyclic graph
if len(adj['A']) == 1 and len(adj['B']) == 1 and len(adj['C']) == 1:
    print("Impossible")
else:
    print(''.join(topological_sort(adj)))
