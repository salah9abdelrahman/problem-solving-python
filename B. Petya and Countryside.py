"""
http://codeforces.com/contest/66/problem/B

1
2

5
1 2 1 2 1

8
1 2 1 1 1 3 3 4

100
1 2 3 4 5 6 7 8 9 10 11 100 88 87 86 85 84 83 82 81 80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 1 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
"""
n = int(input())
s = [int(i) for i in input().split()]
if n == 1:
    print(1)
else:
    result = float('-inf')
    for i in range(n):
        sections = 1
        j = i
        while j > 0:
            if s[j - 1] > s[j]:
                break
            sections += 1
            j -= 1
        j = i
        while j < n - 1:
            if s[j] < s[j + 1]:
                break
            sections += 1
            j += 1
        if sections > result:
            result = sections

    print(result)
