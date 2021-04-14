# deleted 6
arr = [1, 3, 5, 7, 8, 9, 4, 2]
n = len(arr) + 2
visited = [False] * n

for i in arr:
    visited[i] = True

for i in range(1, n):
    if not visited[i]:
        print(i)
