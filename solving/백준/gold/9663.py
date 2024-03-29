# https://www.acmicpc.net/problem/9663

import sys
input = sys.stdin.readline

def check(row):
    for tmp_row in range(row):
        if table[row] == table[tmp_row]:
            return False
        if row - tmp_row == abs(table[row] - table[tmp_row]):
            return False
    return True

def solution(row = 0):
    if row == n:
        global answer
        answer += 1
        return
    for column in range(n):
        if not visited[row]:
            table[row] = column
            if check(row):
                visited[row] = True
                solution(row+1)
                visited[row] = False


n = int(input())

table = [0 for _ in range(n)]
visited = [False for _ in range(n)]
answer = 0

solution()
print(answer)