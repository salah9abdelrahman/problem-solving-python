inp = input().split()
n, m = map(int, inp)
inp = input().split()
xc, yc = map(int, inp)
k = int(input())
steps = 0
ans = 0
for i in range(k):
    inp = input().split()
    x, y = map(int, inp)
    steps = 0
    l, r = 0, max(n, m)
    while l <= r:
        mid = l + (r - l) // 2
        if n >= xc + x * mid > 0 and m >= mid * y + yc > 0:
            steps = mid
            l = mid + 1
        else:
            r = mid - 1
    ans += steps
    xc = x * steps + xc
    yc = y * steps + yc
print(int(ans))
