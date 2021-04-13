"""
https://codeforces.com/contest/365/problem/A

10 6
1234560
1234560
1234560
1234560
1234560
1234560
1234560
1234560
1234560
1234560

2 1
1
10

"""

n, k = (int(i) for i in input().split())
sol = 0
set1 = set(str(i) for i in range(k + 1))
for i in range(n):
    set2 = set(input())
    if set1.issubset(set2):
        sol += 1

print(sol)
