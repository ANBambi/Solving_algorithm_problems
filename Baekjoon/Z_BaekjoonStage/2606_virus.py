import sys
input = sys.stdin.readline

computer = int(input())
network = int(input())

connects = {}

visited = [False for _ in range(computer+1)]
count = 0

for _ in range(network):
    a, b = map(int, input().split())
    if a in connects:
        connects[a].append(b)
    else:
        connects[a] = [b]
    if b in connects:
        connects[b].append(a)
    else:
        connects[b] = [a]
        
def dfs(a):
    visited[a] = True
    if a in connects:
        for b in connects[a]:
            if visited[b] == False:
                dfs(b)

dfs(a = 1)

for a in range(2, computer+1):
    if visited[a]:
        count += 1

print(count)
