# 9663 N-Queen 

'''
완전 탐색 + 백트래킹 방식으로 품
board의 initial state = 0
board에 queen이 놓이면 1
놓인 queen 때문에 특정 부분에 놓으면 안되는 부분 (가로, 세로, 대각선 줄)은 -1로 update
백트래킹 시 board의 -1 부분 다시 0으로 되돌려 놓는 작업은, 각 depth마다 -1되는 좌표들 묶어서 stack에 append시키고 나중에 pop해서 돌려놓기
pypy3시 메모리:185604KB	시간:15820ms로 더 효율적인 코드가 있을거 같음
N 1부터 15 까지의 답 [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
'''

# board에서 1이 몇개있는지, 즉 queen이 몇개 놓여있는지
def list_sum(a: list)->int:
    total = 0
    for i in range(N):
        for j in range(N):
            if a[i][j] == 1:
                total +=1
    return total

# board[depth][i]에 queen이 놓였을때 다른곳 놓으면 안되는 부분 -1 해주기
def set_negative(depth: int, i: int)-> None:
    temp = []
    for k in range(N):

        # 가로줄 처리
        if board[depth][k] == 0:
            board[depth][k] = -1
            temp.append((depth, k))
        
        # 여기서부터는 k 가 depth 보다 작을 때는 신경 안써도 됨. 왜냐 그건 earlier depth에서 처리 됬을거기 때문
        # 세로줄 처리
        if k > depth and board[k][i] == 0:
            board[k][i] = -1
            temp.append((k, i))
        
        # 왼쪽 아래 대각선
        if depth + k <N and 0<= i-k and board[depth+k][i-k] == 0:
            board[depth+k][i-k] = -1
            temp.append((depth+k, i-k))
        
        # 오른쪽 아래 대각선
        if depth + k <N and i+k <N and board[depth+k][i+k] == 0:
            board[depth+k][i+k] = -1
            temp.append((depth+k, i+k))

    #stack에 넣어줘서 나중에 백트래킹 순서 시 pop해서 그 좌표들 다시 0 으로 만들어주기
    stack.append(temp)

# 메인 완전탐색 함수
def chess(depth =0)-> int:
    global cnt
    
    # 마지막 줄까지 채워졌을 때 N개의 퀸이 놓여졌는지 확인
    if depth == N:
        if list_sum(board) == N:
            cnt += 1
            return
    else:
        for i in range(N):
            if board[depth][i] == 0:

                # queen 놓고, -1값들 넣어주고 다음 depth값으로 recursion진입해서 완전탐색
                board[depth][i] = 1
                set_negative(depth, i)

                chess(depth+1)

                # 백트래킹 나왔을 시, 다시 이 depth level에서 -1된 좌표들 원상복귀
                board[depth][i] = 0
                reverse = stack.pop()
                for do in reverse:
                    y, x = do
                    board[y][x] = 0
    return cnt

if __name__ == '__main__':

    N = int(input())
    board = [[0]*N for _ in range(N)]
    cnt = 0
    stack = []
    ans = chess()
    print(ans)