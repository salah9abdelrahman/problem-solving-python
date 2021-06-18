"""
4
RLRL
2 4 6 10


3
LLR
40 50 60


4
LRLR
2 4 8 10


5
LRLRL
2 4 16 20 22


5
LRRRL
2 4 16 20 22


"""
n = int(input())
dirs = input()
first_right = dirs.index("R")
last_left = dirs.rfind("L")
bens = [int(i) for i in input().split()]
dirs = dirs[first_right:last_left + 1]
bens = bens[first_right:last_left+1]

left = []
right = []
for i in range(len(dirs)):
    if dirs[i] == 'R':
        right.append(bens[i])
    else:
        left.append(bens[i])

if len(right) == 0 or len(left) == 0:
    print(-1)

else:
    res = float('inf')
    r, l = 0, 0
    for i in left:
        for j in right:
            dis = abs(i - j) // 2
            if dis < res:
                r, l = i, j
                res = dis
    print(res)
    print(r, l)
    print(right)
    print(left)
    b = abs(min(right) - min(left)) // 2
    print(b)
