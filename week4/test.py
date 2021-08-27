#(7) - 2098 외판원 순회

#(8) - 2253 점프

import sys
sys.stdin = open('week4/input.txt')
input = sys.stdin.readline

# N: 마지막 돌, M: 못 밟는 돌 개수
N, M = map(int, input().split())

# 못 밟는 돌 저장
blocked = []
for _ in range(M):
    blocked.append(int(input()))

# 해당 rock에서 나올 수 있는 최대 점프 거리
# 앞으로 밖에 갈 수 없기 때문에 10을 가야된다면 나올 수 있는 최대 점프 거리는 arithmetic series로 1,2,3,4 '4'임
def min_arith(n):
    return int((n*2)**0.5) +1

s = min_arith(N)
rock = [[N]*(s+1) for _ in range(N+1)]
rock[1][0] = 0

for i in range(2, N+1):
    if i in blocked:
        continue
    for j in range(1, min_arith(i)):
        rock[i][j] = min(rock[i-j][j-1], rock[i-j][j], rock[i-j][j+1]) +1

for i in range(len(rock)):
    print(i, rock[i])
# ans = min(rock[-1]) 
# if ans == N:
#     print(-1)
# else:
#     print(ans)