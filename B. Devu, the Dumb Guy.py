"""
http://codeforces.com/contest/439/problem/B
"""

n1 = input().split()
n2 = input().split()
n, x = (int(i) for i in n1)
arr = [int(i) for i in n2]
arr = sorted(arr)
res = 0
for i in range(n):
    res = res + (arr[i] * x)
    if x > 1:
        x -= 1

print(res)
