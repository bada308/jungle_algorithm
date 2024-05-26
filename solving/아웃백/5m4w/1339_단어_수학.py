'''
https://www.acmicpc.net/problem/1339
'''
import sys
input = sys.stdin.readline

n = int(input())
strings = [input().strip() for _ in range(n)]

positions = dict()

for string in strings:
    for idx, char in enumerate(string[::-1]):
        positions[char] = positions.get(char, 0) + 10 ** idx

position_list = sorted(list(positions.items()),
                       key=lambda x: x[1], reverse=True)

for idx, (c, _) in enumerate(position_list):
    positions[c] = 9 - idx


for i in range(n):
    for key, value in positions.items():
        strings[i] = strings[i].replace(key, str(value))
    strings[i] = int(strings[i])
print(sum(strings))
