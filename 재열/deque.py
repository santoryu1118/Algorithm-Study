from sys import stdin

n = int(input())

stack = []
for temp in map(int, stdin):
    if not temp and stack:
        stack.pop()
    else:
        stack.append(temp)
print(sum(stack))