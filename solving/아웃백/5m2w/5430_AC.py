'''
https://www.acmicpc.net/problem/5430
'''
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    command = list(input().strip())
    n = int(input())
    nums = input().strip().replace(
        "[", "").replace("]", "")
    if nums:
        nums = deque(list(map(int, nums.split(","))))
    else:
        nums = deque([])
    r_count = 0
    is_start = True
    result = ""

    for c in command:
        if c == "R":
            is_start = not is_start
        if c == "D":
            if not len(nums):
                result = "error"
                break
            if is_start:
                nums.popleft()
            else:
                nums.pop()
    if result == "error":
        print("error")
    else:
        print("[", end="")
        if is_start:
            print(*nums, sep=",", end="")
        else:
            nums.reverse()
            print(*nums, sep=",", end="")
        print("]")
