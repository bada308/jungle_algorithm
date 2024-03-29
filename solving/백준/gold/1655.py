# https://www.acmicpc.net/problem/1655

'''
가운데를 말해요.

사용자가 수를 입력하면 그 값을 배열에 저장하고, 배열의 중앙값을 출력하는 문제

힙 두 개를 이용해서 구할 수 있다.

중앙값의 왼쪽을 저장하는 힙 : left (최대 힙)
중앙값의 오른쪽을 저장하는 힙 : right (최소 힙)

중앙값이 2개일 때는 둘 중 작은 수를 출력하기 때문에, 출력 시 left의 root를 출력합니다.
만약 right에 left의 최댓값 보다 작은 값이 포함되어 있으면 서로의 root를 교환합니다.
'''

import sys
import heapq
input = sys.stdin.readline

n = int(input())

left, right = [], []

for _ in range(n):
    num = int(input())
    if len(left) == len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)
    
    if left and right and left[0] * -1 > right[0]:
        tmp1 = heapq.heappop(left) * -1
        tmp2 = heapq.heappop(right)
        
        heapq.heappush(left, tmp2 * -1)
        heapq.heappush(right, tmp1)
    
    print(-left[0])