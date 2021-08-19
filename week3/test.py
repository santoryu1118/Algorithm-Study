#(1) - 1260 DFS와 BFS
import sys
# N: vertex, M: edge, V: start vertex
N, M, V = map(int, sys.stdin.readline().split())
adj = [[0]*(N+1) for _ in range(N+1)]
for _ in range(N):
    a,b = map(int, sys.stdin.readline().split())
    adj[a][b] = adj[b][a] = 1

print(adj)
# def dfs():