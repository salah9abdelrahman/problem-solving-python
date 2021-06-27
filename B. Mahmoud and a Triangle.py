"""https://codeforces.com/contest/796/problem/B"""

n = int(input())
inp = input()
arr = [int(i) for i in inp.split()]
arr.sort()

for i in range(n - 2):
    if arr[i] + arr[i + 1] > arr[i + 2]:
        print("YES")
        exit(0)
print("NO")
