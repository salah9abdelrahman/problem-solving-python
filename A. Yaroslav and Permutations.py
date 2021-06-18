"""
http://codeforces.com/contest/296/problem/A
"""

n = int(input())
nums = [int(i) for i in input().split()]
flag = True
for i in nums:
    len_i = nums.count(i)
    len_other = len(nums) - len_i
    if len_i - len_other > 1:
        flag = False
        break
if flag:
    print("YES")
else:
    print("NO")
