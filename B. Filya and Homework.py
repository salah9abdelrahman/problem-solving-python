"""https://codeforces.com/contest/714/problem/B"""
n = input()
inp = input()

arr = set(map(int, inp.split()))

if len(arr) <= 2:
    print('YES')
    exit()

if len(arr) > 3:
    print('NO')
    exit()

# we have 3 distinct numbers
arr = list(arr)
arr.sort()
if abs(arr[0] - arr[1]) == abs(arr[2] - arr[1]):
    print('YES')

else:
    print('NO')
