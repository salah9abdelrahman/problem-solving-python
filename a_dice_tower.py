"""
http://codeforces.com/contest/225/problem/A

3
6
3 2
5 4
2 4

3
3
2 6
4 1
5 3


"""
TOTALSUM = sum([1, 2, 3, 4, 5, 6])
n = int(input())
top = int(input())
possible = True
for i in range(n):
    s1a, s2a = (int(s) for s in input().split())
    s1b, s2b = 7 - s1a, 7 - s2a
    sides = [top, s1a, s2a, s1b, s2b]
    down = TOTALSUM - sum(sides)
    if down in sides:
        possible = False
        break
    top = down
    down = top

if possible:
    print("YES")
else:
    print("NO")
