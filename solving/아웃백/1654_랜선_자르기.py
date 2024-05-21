'''
https://www.acmicpc.net/problem/1654
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lans = [int(input()) for _ in range(n)]

start = 1
end = max(lans)

while start <= end:
    mid = (start + end) // 2
    count = 0

    # 길이가 mid일 때 만들 수 있는 랜선의 개수 세기
    for lan in lans:
        count += (lan // mid)

    # 만들 수 있는 개수가 목표치보다 많으면 길이 늘리기
    if count >= k:
        start = mid + 1
    # 적으면 길이 줄이기
    else:
        end = mid - 1

print(end)
