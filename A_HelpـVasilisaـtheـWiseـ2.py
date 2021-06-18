r1, r2 = (int(s) for s in input().split())
c1, c2 = (int(s) for s in input().split())
d1, d2 = (int(s) for s in input().split())
found = False
for w in range(1, 10):
    for x in range(1, 10):
        for y in range(1, 10):
            for z in range(1, 10):
                if len(set([w, x, y, z])) == 4 and w + x == r1 and w + y == c1 and w + z == d1 and x + z == c2 and y + z == r2 and x + y == d2:
                    found = True
                    print(w, x)
                    print(y, z)

if not found:
    print(-1)
