"""
http://codeforces.com/contest/16/problem/B
"""

n, m = (int(i) for i in input().split())
boxes = []
matches = []
for i in range(m):
    boxes_num, matches_num = (int(i) for i in input().split())
    boxes.append(boxes_num)
    matches.append(matches_num)

result = 0
while n > 0:
    if not boxes:
        break
    max_matches = max(matches)
    max_index = matches.index(max_matches)
    result += (max_matches * boxes[max_index])
    n -= boxes[max_index]
    if n < 0:
        result -= (abs(n) * matches[max_index])
    matches.pop(max_index)
    boxes.pop(max_index)

print(result)
