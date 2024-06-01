'''
https://www.acmicpc.net/problem/14889
'''
import sys
input = sys.stdin.readline

n = int(input())
table = [list(map(int, input().split())) for __ in range(n)]

answer = int(1e8)


def calc_score(team):
    score = 0
    for i in team:
        for j in team:
            score += table[i][j]
    return score


def backtrack(before, start_team):
    global answer

    if before == n-1:
        return

    if len(start_team) == n // 2:
        link_team = set(range(n)) - start_team
        start_score = calc_score(start_team)
        link_score = calc_score(link_team)
        answer = min(answer, abs(start_score - link_score))
        return

    backtrack(before + 1, start_team)
    backtrack(before + 1, start_team | {before + 1})


backtrack(-1, set())
print(answer)
