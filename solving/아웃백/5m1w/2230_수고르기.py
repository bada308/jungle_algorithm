'''
https://www.acmicpc.net/problem/2230
'''
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums.sort()  # 투 포인터 사용을 위해 정렬

start = 0
end = 1
answer = nums[-1] - nums[0]

while end < n and start < n:
    gap = nums[end] - nums[start]

    # 차이가 m보다 작은 경우 end 증가
    if gap < m:
        end += 1
    # 차이가 m보다 큰 경우 answer 갱신 후 start 증가
    else:
        answer = min(answer, gap)
        start += 1

print(answer)
