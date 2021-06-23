"""
https://codeforces.com/contest/492/problem/B
"""
n, l = (int(i) for i in input().split())
arr = [int(i) for i in input().split()]
arr = sorted(arr)
first = arr[0]
last = arr[-1]
if arr[0] == 0 and n > 1:
    first = (arr[0] + arr[1]) // 2
mid = 0
last = l - last
for i in range(n - 1):
    val = arr[i + 1] - arr[i]
    if val > mid:
        mid = val

# print(first, mid, last)
print(max([first, mid / 2, last]))
