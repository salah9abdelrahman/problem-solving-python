"""
https://codeforces.com/contest/102/problem/B
"""
n = input()
result = 0
while int(n) >= 10:
    arr = []
    for i in str(n):
        arr.append(i)
    n = sum([int(i) for i in arr])
    result += 1

print(result)
