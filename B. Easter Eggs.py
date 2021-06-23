"""
https://codeforces.com/contest/78/problem/B
"""
n = int(input())
s = "ROYGBIV"
dis = "GBIV"
sol = s + (dis * (((n - 7) // 4) + 1))

print(sol[:n])
