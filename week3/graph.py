#(1) - 1260 DFS와 BFS
import sys
from collections import deque
# N: vertex, M: edge, V: start vertex
N, M, V = map(int, sys.stdin.readline().split())

# 인접 행렬 만듬
# vertex 가 1부터 시작하기 때문에 N+1 행렬
adj = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    adj[a][b] = adj[b][a] = 1

# 방문 list 생성
dfs_visit = [0] * (N+1)
bfs_visit = [0] * (N+1)

def dfs(V):   # stack 개념 LIFO
    dfs_visit[V] = 1
    print(V, end=' ')

    for i in range(1, N+1):
        if adj[V][i] == 1 and dfs_visit[i] == 0:
            dfs(i)

def bfs(V):  # queue 개념 FIFO
    bfs_visit[V] = 1
    que = deque()
    que.append(V)

    while que:
        front = que.popleft()
        print(front, end = ' ')    
        for i in range(1, N+1):
            if adj[front][i] == 1 and bfs_visit[i] == 0:
                que.append(i)
                bfs_visit[i] = 1

dfs(V)
print()
bfs(V)
