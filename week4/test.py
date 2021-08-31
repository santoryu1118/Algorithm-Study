#(13) - 1700 멀티탭 스케줄링

import sys
# sys.stdin = open('week4/input.txt')
input = sys.stdin.readline

# N: 멀티탭 구멍 개수  K: 전기용품 총 사용횟수
N, K = map(int, input().split())

schedule = list(map(int, input().split()))
outlet = []
cnt = 0

for i in range(K):
    # 멀티탭이 비어있을 경우
    if len(outlet) < N and schedule[i] not in outlet:
        outlet.append(schedule[i])
    # 멀티탭에 이미 해야되는 작업이 꽂혀있을 경우
    elif schedule[i] in outlet:
        continue
    # 빼고 꽂아야 하는 경우
    else:
        cnt += 1
        finish = False
        for j in range(len(outlet)):
            if outlet[j] not in schedule[i+1:]:
                outlet.remove(outlet[j])
                outlet.append(schedule[i])
                finish = True
                break
        if finish:
            continue
        
        latest = 0
        for j in range(len(outlet)):
            latest = max(latest, schedule[i+1:].index(outlet[j])+ i+1)
        outlet.remove(schedule[latest])
        outlet.append(schedule[i])
        
print(cnt)