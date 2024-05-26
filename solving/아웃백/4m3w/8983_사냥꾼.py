'''
https://www.acmicpc.net/problem/8983

'''
import sys
input = sys.stdin.readline

m, n, l = map(int, input().split())
position = sorted(list(map(int, input().split())))
animals = [list(map(int, input().split())) for _ in range(n)]

answer = 0

for animal in animals:
    a, b = animal

    MIN = a + b - l
    MAX = a - b + l

    start = 0
    end = len(position) - 1

    while start <= end:
        mid = (start + end) // 2
        if MIN <= position[mid] <= MAX:
            answer += 1
            break
        elif position[mid] < MIN:
            start = mid + 1
        else:
            end = mid - 1

print(answer)
