"""
https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=380

e2 e4
a1 b2
b2 c3
a1 h8
a1 h7
h8 a1
b1 c3
f6 f6

"""
from collections import deque

KNIGHT_MOVES = [(2, 1), (2, -1), (-2, -1), (-2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
BOARD_NUM = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}


def is_valid_cell(num):
    return 0 < num[0] <= 8 and 0 < num[1] <= 8


def bfs(s, e):
    search_queue = deque()
    search_queue.append(s)
    _path = {}
    visited = set()
    visited.add(s)
    while search_queue:
        current = search_queue.popleft()
        if current == e:
            return _path

        for i in KNIGHT_MOVES:
            neighbor = current[0] + i[0], current[1] + i[1]
            if is_valid_cell(neighbor) and neighbor not in visited:
                _path[neighbor] = current
                visited.add(neighbor)
                search_queue.append(neighbor)


if __name__ == '__main__':
    inp = input().split()
    while inp:
        start = int(inp[0][1]), BOARD_NUM[inp[0][0]]
        goal = int(inp[1][1]), BOARD_NUM[inp[1][0]]
        path = bfs(start, goal)
        curr = goal
        movies = 0
        correct = []
        while curr != start:
            correct.append(curr)
            movies += 1
            curr = path[curr]
        print(f'To get from {inp[0]} to {inp[1]} takes {movies} knight moves.')
        inp = input().split()
