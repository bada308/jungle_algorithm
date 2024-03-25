# https://www.acmicpc.net/problem/2630

import sys
input = sys.stdin.readline

n = int(input())
init_paper = [list(map(int, input().split())) for _ in range(n)]

def is_all_same(paper, value):
    return all(all(x == value for x in row) for row in paper)

def getColoredPaper(size, paper):
    if is_all_same(paper, 0):
        global white_count
        white_count += 1
        return
    
    if is_all_same(paper, 1):
        global blue_count
        blue_count += 1
        return
    
    half = size // 2
    
    top = paper[:half]
    getColoredPaper(half, [row[:half] for row in top])
    getColoredPaper(half, [row[half:] for row in top])
    
    bottom = paper[half:]
    getColoredPaper(half, [row[:half] for row in bottom])
    getColoredPaper(half, [row[half:] for row in bottom])

white_count = 0
blue_count = 0

getColoredPaper(n, init_paper)
print(white_count)
print(blue_count)