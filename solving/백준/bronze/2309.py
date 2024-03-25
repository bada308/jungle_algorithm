# https://www.acmicpc.net/problem/2309

import sys
from itertools import combinations
input = sys.stdin.readline

dwarf_list = [int(input()) for _ in range(9)]
case7 = list(combinations(dwarf_list, 7))

for c in case7:
    if sum(list(c)) == 100:
        print(*sorted(c), sep="\n")
        break