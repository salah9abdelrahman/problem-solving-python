"""https://codeforces.com/contest/796/problem/B"""
inp = input()
n, m, k = map(int, inp.split())
holes = set(input().split())
bone = '1'
for i in range(k):
    if bone in holes:
        break
    u, v = input().split()
    if bone == u:
        bone = v
    elif bone == v:
        bone = u
print(bone)
