'''
https://www.acmicpc.net/problem/1700
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
sequence = list(map(int, input().split()))

tap = set()
count = 0

for i in range(k):
    item = sequence[i]
    # 멀티탭이 비어있거나 이미 꽂혀있는 경우
    if item in tap:
        continue
    if len(tap) < n:
        tap.add(item)
        continue

    use_set = set()
    use_list = []

    for next in sequence[i+1:]:
        if next in tap and next not in use_set:
            use_set.add(next)
            use_list.append(next)

    empty = tap - use_set
    if empty:
        tap.remove(empty.pop())
        tap.add(item)
    else:
        tap.remove(use_list[-1])
        tap.add(item)

    count += 1

print(count)
