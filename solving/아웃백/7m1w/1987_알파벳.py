'''
https://www.acmicpc.net/problem/1987
'''
import sys
input = sys.stdin.readline

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]


r, c = map(int, input().split())
board = [list(input().strip()) for __ in range(r)]
visited = [False] * 26

answer = 0


def backtracking(i, j, curr):
    global answer
    answer = max(answer, curr)
    if answer >= 26 or answer >= r*c:
        return

    for di, dj in direction:
        ci, cj = i + di, j + dj
        if 0 <= ci < r and 0 <= cj < c:
            idx = ord(board[ci][cj]) - ord('A')
            if not visited[idx]:
                visited[idx] = True
                backtracking(ci, cj, curr + 1)
                visited[idx] = False


visited[ord(board[0][0]) - ord('A')] = True
backtracking(0, 0, 1)
print(answer)
