"""
http://codeforces.com/contest/451/problem/B
"""

n = int(input())
n1 = input()
arr = [int(i) for i in n1.split()]
count = 0
sol1, sol2 = -1, -1
sorted_arr = sorted(arr)

for i in range(len(arr)):
    if arr[i] != sorted_arr[i]:
        if sol1 == -1:
            sol1 = i
        else:
            sol2 = i

solved = True
for i, j in zip(range(sol1, sol2), range(sol2, sol1, -1)):
    if sorted_arr[i] != arr[j]:
        solved = False
        break

if solved:
    print('yes')
    if sol1 == -1:
        print(1, 1)
    else:
        print(sol1 + 1, sol2 + 1)
else:
    print('no')
