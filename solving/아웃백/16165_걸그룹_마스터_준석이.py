'''
https://www.acmicpc.net/problem/16165
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
girls = dict()

for _ in range(n):
    team = input().strip()
    girls[team] = set()
    count = int(input())
    for _ in range(count):
        member = input().strip()
        girls[team].add(member)

for _ in range(m):
    name = input().strip()
    type = int(input())

    if type:
        for team, members in girls.items():
            if name in members:
                print(team)
                break
    else:
        result = sorted(list(girls[name]))
        print(*result, sep="\n")
