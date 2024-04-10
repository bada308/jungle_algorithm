'''
https://www.acmicpc.net/problem/1541
잃어버린 괄호
'''

import sys
input = sys.stdin.readline

nums = input().strip().split("-")
nums = list(map(lambda s: s.split("+"), nums))
nums = [[int(num) for num in sublist] for sublist in nums]

answer = sum(nums[0])

for i in range(1, len(nums)):
    answer -= sum(nums[i])


print(answer)