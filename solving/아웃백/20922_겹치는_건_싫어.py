'''
https://www.acmicpc.net/problem/20922
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

counts = [0] * (max(nums) + 1)
answer = 0

start, end = 0, 0

while end < n:
    if counts[nums[end]] < k:   # count 개수가 조건에 부합하는 경우
        counts[nums[end]] += 1  # nums[end] 증가
        end += 1                # end 증가
    else:                           # 조건을 위반하는 경우
        counts[nums[start]] -= 1    # nums[start] 감소
        start += 1                  # start 증가
    answer = max(answer, end - start)  # 필요 시, answer 갱신

print(answer)
