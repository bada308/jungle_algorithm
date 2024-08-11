'''
https://www.acmicpc.net/problem/30804
'''
"""import sys
input = sys.stdin.readline

n = int(input())
fruits = list(map(int, input().split()))

fruit_map = dict()

for f in fruits:
    if f in fruit_map:
        fruit_map[f] += 1
    else:
        fruit_map[f] = 1

start, end = 0, n - 1
answer = n

while start < end:
    if len(fruit_map) <= 2:
        break
    start_fruit = fruits[start]
    end_fruit = fruits[end]
    if fruit_map[start_fruit] > fruit_map[end_fruit]:
        if fruit_map[end_fruit] > 1:
            fruit_map[end_fruit] -= 1
        else:
            del fruit_map[end_fruit]
        end -= 1
    else:
        if fruit_map[start_fruit] > 1:
            fruit_map[start_fruit] -= 1
        else:
            del fruit_map[start_fruit]
        start += 1
    answer -= 1

print(answer)"""

# 브루트포스 방식으로 풀어야한당~~

import sys
input = sys.stdin.readline

n = int(input())
fruits = list(map(int, input().split()))
fruit_map = dict()

left, right, answer = 0, 0, 0

while right < n:
    right_fruit = fruits[right]
    if right_fruit in fruit_map:
        fruit_map[right_fruit] += 1
    else:
        fruit_map[right_fruit] = 1
    
    while len(fruit_map) > 2:
        left_fruit = fruits[left]
        if fruit_map[left_fruit] > 1:
            fruit_map[left_fruit] -= 1
        else:
            del fruit_map[left_fruit]
        left += 1
    
    answer = max(answer, right - left + 1)
    right += 1

print(answer)