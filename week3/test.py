#(10) - 2617 구슬찾기

import sys

N, M = map(int, sys.stdin.readline().split())

# 인덱스보다 큰 값들 저장
bigger = [[] for _ in range(N+1)]
# 인덱스보다 작은 값들 저장
smaller = [[] for _ in range(N+1)]

for _ in range(M):
    big, small = map(int, sys.stdin.readline().split())
    bigger[small].append(big)
    smaller[big].append(small)

# print(f'bigger: {bigger}')
# print(f'smaller: {smaller}')

ans_list = []
