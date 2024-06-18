'''
https://www.acmicpc.net/problem/2343
'''
import sys
input = sys.stdin.readline


def getCount(size):
    global times
    count = 1
    curr = 0
    for t in times:
        if curr + t > size:
            count += 1
            curr = 0
        curr += t
    return count


n, m = map(int, input().split())

times = list(map(int, input().split()))
start = max(times)
end = sum(times)

while start <= end:
    mid = (start + end) // 2
    if getCount(mid) > m:
        start = mid + 1
    else:
        end = mid - 1

print(start)
