import sys
n,k = map(int, sys.stdin.readline().split())
N = [x for x in range(1,n+1)]
answer = []
num = 0
for _ in range(n):
    num = (num + k-1)%len(N)
    answer.append(str(N.pop(num)))

print('<', ', '.join(answer), '>', sep ='')
