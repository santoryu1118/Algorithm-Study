import sys
from collections import deque

# 2차원 지도 생성
N = int(sys.stdin.readline())
MAP = [[0]*N for _ in range(N)]
MAP[0][0] = 'snake'

# 지도에 apple 추가
k = int(sys.stdin.readline())
for _ in range(k):
    y,x, = map(int, sys.stdin.readline().split())
    MAP[y-1][x-1] = 'apple'

# instruction 딕셔너리 key에는 몇번째 move인지 저장되있고 value에는 그 move의 방향 저장
L = int(sys.stdin.readline())
instruction = {}
for _ in range(L):
    num, dir = sys.stdin.readline().split()
    instruction[int(num)] = dir

# 방향 관련
#   3
# 2   0
#   1
def DIR(current_dir, new_dir):
    #오른쪽
    if new_dir == 'D':
        dir = (current_dir + 1)%4
    #왼쪽
    elif new_dir == 'L':
        dir = (current_dir - 1)%4
    return dir

#dir= 0  1  2   3 일때 x,y 좌표가 어떻게 바뀌는지  
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

'''
게임 설명
1. 머리 다음칸에 위치
2. 사과 있다면 꼬리 안움직임
3. 없다면 꼬리 popleft됨
% 꼬리 물거나 벽 닿으면 game over %
'''
snake = deque([(0,0)])  # snake 좌표들 저장해놓는 deque

def game():
    y = x = 0  # initial pos
    dir = 0    # initial direction
    time_count = 0  # initial time_count

    while True:
        time_count +=1
        y += dy[dir]
        x += dx[dir]

        # game over 되는 상황
        if not 0 <= y < N or not 0 <=x < N or MAP[y][x] == 'snake':
            return time_count

        if MAP[y][x] == 0:
            pop_y, pop_x= snake.popleft()
            MAP[pop_y][pop_x] = 0
        snake.append((y,x))
        MAP[y][x] = 'snake'
        
        if time_count in instruction.keys():
            dir = DIR(dir, instruction[time_count])
    
print(game())
    



