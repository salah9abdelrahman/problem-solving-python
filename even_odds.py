"""
https://codeforces.com/contest/318/problem/A

category: math

10 3

10 7

7 7

"""

n, k = (int(i) for i in input().split())
result = 0
mid = n // 2 if n % 2 == 0 else n // 2 + 1
# if k is odd
if mid >= k:
    result = k * 2 - 1

else:
    result = (k - mid) * 2

print(result)
