"""https://codeforces.com/contest/88/problem/B"""
import math

MAX_DIS = float('inf')


class Letter:
    def __init__(self, symbol, r, c):
        self.symbol = symbol
        self.r = r
        self.c = c
        self.distance_from_s = MAX_DIS

    def __str__(self):
        return 'symbol: ' + self.symbol + " r: " + str(self.r) + " c: " + str(self.c) + " distance: " + str(
            self.distance_from_s)

    def __repr__(self):
        return 'symbol: ' + self.symbol + " r: " + str(self.r) + " c: " + str(self.c)

    def get_distance_from_s(self, shifts):
        if self.distance_from_s == float('inf'):
            for shift in shifts:
                distance = math.sqrt(((shift.r - self.r) ** 2) + ((shift.c - self.c) ** 2))
                if distance < self.distance_from_s:
                    self.distance_from_s = distance
        return self.distance_from_s

    def __eq__(self, other):
        return self.r == self.r and self.c == self.c


inp = input()
n, m, x = map(int, inp.split())
keyboard = {}

for i in range(n):
    inp = input()
    for j in range(len(inp)):
        letter = Letter(inp[j], i, j)
        key_letter = keyboard.get(inp[j])
        if key_letter:
            key_letter.append(letter)
        else:
            keyboard[inp[j]] = []
            keyboard[inp[j]].append(letter)

q = int(input())
t = input()
solvable = True
sol = 0
shifts = keyboard.get("S")
keyboard_short_moves = {}
if shifts:
    for key in keyboard:
        key_letters = keyboard[key]
        distance_each_letter = MAX_DIS
        for letter in key_letters:
            letter_key_distance = letter.get_distance_from_s(shifts)
            if letter_key_distance < distance_each_letter:
                distance_each_letter = letter_key_distance
        keyboard_short_moves[key] = distance_each_letter

for i in range(q):
    letter = t[i]
    letter_lower = letter.lower()
    key_short_distance = keyboard_short_moves.get(letter_lower)
    if keyboard.get(letter_lower):
        if letter.isupper():
            if not shifts:
                solvable = False
                break

            if key_short_distance > x:
                sol += 1
    else:
        solvable = False
        break

if solvable:
    print(sol)
else:
    print(-1)
