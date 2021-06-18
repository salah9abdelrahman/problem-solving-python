"""
2 3
1 2
3 4


3 7
1 2
3 3
4 7

"""
n, k = (int(i) for i in input().split())
segs = 0
for i in range(n):
    s1, s2 = (int(s) for s in input().split())
    segs += s2 - s1 + 1

result = segs % k
if result == 0:
    print(result)
else:
    result = k - result
    print(result)
