#(7) - 1987 알파벳

import sys

R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]

# visit = [[False]*C for _ in range(R)]
# visit[0][0] = True

trace =[board[0][0]]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

cnt = 1

def dfs(y, x):
    global cnt

    for i in range(4):
        newy, newx = y + dy[i], x + dx[i]
        if 0 <= newy < R and 0 <= newx < C: 
            if board[newy][newx] not in trace:
                trace.append(board[newy][newx])
                dfs(newy, newx)
                trace.pop()
            else:
                cnt = max(cnt, len(trace))
                continue
    return

dfs(0,0)
print(cnt)