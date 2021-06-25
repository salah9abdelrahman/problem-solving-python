"""
http://codeforces.com/contest/363/problem/B
"""
n1 = input().split()
n, k = (int(i) for i in n1)
n2 = input().split()
arr = [int(i) for i in n2]
min_width = float('inf')
sol = 1

arr.insert(0, 0)

for i in range(1, len(arr)):
    arr[i] += arr[i - 1]

for i in range(k, n + 1):
    idx = i - k
    val = arr[i] - arr[idx]
    if val < min_width:
        min_width = val
        sol = idx + 1

print(sol)
