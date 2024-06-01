'''
https://www.acmicpc.net/problem/14889
'''
import sys
input = sys.stdin.readline

n = int(input())
table = [list(map(int, input().split())) for __ in range(n)]

answer = int(1e8)


def back(before, start_team):
    global answer
    if before == n-1:
        return
    if len(start_team) == n // 2:
        answer = min(answer, check(start_team))
        return
    back(before + 1, start_team)
    start_team.add(before + 1)
    back(before+1, start_team)
    start_team.remove(before + 1)


def check(start_team):
    link_team = set([i for i in range(n)]) - start_team
    start_sum, link_sum = 0, 0

    for j in range(n):
        if j in start_team:
            for k in range(n):
                if j == k:
                    continue
                if k in start_team:
                    start_sum += table[j][k]
        else:
            for k in range(n):
                if j == k:
                    continue
                if k in link_team:
                    link_sum += table[j][k]

    return abs(start_sum - link_sum)


back(-1, set())
print(answer)
