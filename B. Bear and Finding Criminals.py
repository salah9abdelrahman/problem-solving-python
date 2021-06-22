"""
6 3
1 1 1 0 1 0

5 2
0 0 0 1 0

"""

n, a = (int(i) for i in input().split())
arr = [i for i in input().split()]
a -= 1
result = int(arr[a])
i = a - 1
j = a + 1

while i >= 0 and j < n:
    if arr[i] == '1' and arr[j] == '1':
        result += 2
    i -= 1
    j += 1

for x in range(i, -1, -1):
    if arr[x] == '1':
        result += 1

for x in range(j, n):
    if arr[x] == '1':
        result += 1
print(result)

# 17 6
# 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1

