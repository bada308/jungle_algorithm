# https://www.acmicpc.net/problem/1978

import math

def getPrime(num):
    result = [False, False] + [True] * (num - 1)
    
    for i in range(2, int(math.sqrt(num)) + 1):
        for j in range(i * 2, num + 1, i):
                result[j] = False
    return result

prime100 = getPrime(1000)

n = int(input())
nums = list(map(int, input().split()))

answer = 0

for num in nums:
    if prime100[num]:
        answer += 1

print(answer)