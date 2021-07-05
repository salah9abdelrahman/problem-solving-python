"""
https://codeforces.com/contest/476/problem/B
"""
import math


def combination(n, k):
    return (math.factorial(n) / (math.factorial(k) * math.factorial(n - k))) / 2 ** n


s1 = input()
s2 = input()
plus1, minus1 = 0, 0
plus2, minus2 = 0, 0
missed = 0
for i in s1:
    if i == '+':
        plus1 += 1
    else:
        minus1 += 1

for i in s2:
    if i == '+':
        plus2 += 1
    elif i == '-':
        minus2 += 1
    else:
        missed += 1

missed_plus, missed_minus = plus1 - plus2, minus1 - minus2
if missed_plus < 0 or missed_minus < 0:
    print(0.0)
else:
    sol = combination(missed, missed_plus)
    print(sol)
