"""
http://codeforces.com/contest/746/problem/B

5
logva

2
no


4
abba


"""
n = int(input())
s = input()
s1, s2 = '', ''


j = 0
for i in range(n - 1, -1, -1):
    if j % 2 == 0:
        s1 += s[i]
    else:
        s2 += s[i]
    j += 1

result = s2 + s1[::-1]
print(result)
