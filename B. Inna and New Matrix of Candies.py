n, m = map(int, input().split())
end = m - 1
MAX = float('inf')
arr = set()
for i in range(n):
    inp = input()
    last_g = inp.rfind('G')
    if last_g == -1:
        last_g = MAX
    last_s = inp.rfind('S')
    if last_s == -1:
        last_s = MAX
    if last_s != MAX and last_g != MAX and last_s > last_g:
        arr.add(last_s - last_g)
    if last_s < last_g:
        print(-1)
        quit()

print(len(arr))
