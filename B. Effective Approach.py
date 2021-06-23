"""
https://codeforces.com/contest/227/problem/B
"""
n = int(input())
arr = input().split()
arr_dict = {int(arr[index]): index + 1 for index in range(n)}
m = int(input())
e = [int(i) for i in input().split()]
w1, w2 = 0, 0
for i in range(m):
    element = arr_dict.get(e[i])
    w1 += element
    w2 += n - element + 1
print(w1, w2)
