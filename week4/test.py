# 1967 - 트리의 지름

import sys
sys.setrecursionlimit(10**6)
input =sys.stdin.readline
n = int(input())

info = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    info[parent].append((child, weight))

# info []
#             1              2             3                 4                5                      6              
# [[], [(2, 3), (3, 2)], [(4, 5)], [(5, 11), (6, 9)], [(7, 1), (8, 7)], [(9, 15), (10, 4)], [(11, 6), (12, 10)], [], [], [], [], [], []]

# 가장 긴 거리를 저장해놓는 global 변수
max_len = 0

def dfs(v):
    global max_len

    if len(info[v]) == 0:
        return 0

    if len(info[v]) > 0:
        list = []
        for nodes in info[v]:
            child, weight = nodes
            # 해당 weight와 그 child tree의 최대 길이 더한 값을 저장
            list.append(weight + dfs(child))
        
        list.sort(reverse = True)
        if len(list) >1:
            # 그중에 제일 큰 값 두개 더해서 max_len과 비교
            max_len = max(max_len, list[0]+list[1])
        else:
            # 이걸 해주는 이유는 child가 하나밖에 없어도 해당 vertex까지 연결되는 거리가 max_len 일 수 있기 때문
            # 즉, 꼭 leaf node 두개의 거리가 max가 아닐 수도 있다는 소리. leaf node와 vertex까지의 거리가 그 부분에서 가장 긴 거리일 수도 있다.
            # list[0] + list[1]이 아니어도 list[0]만으로도 max_len 거리 갱신 가능
            max_len = max(max_len, list[0])

        # 해당 vertex에서 가장 긴값 return
        return list[0] 

# 루트 노드의 번호는 항상 1이라 가정
dfs(1)
print(max_len)

