from collections import deque

N, M, V = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1 # 두 점이 연결되어 있을때
    graph[b][a] = 1
    
visited1 = [0] * (N+1) # +1 안하면 0번째에 집어넣어야함, 
visited2 = visited1.copy()

def dfs(V):
    visited1[V] = 1
    print(V, end= ' ')
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited1[i] == 0:
            dfs(i)

def bfs(V):
    queue = deque([v])
    visited2[V] = 1
    
    while queue:
        V = queue.popleft()
        print(V, end=' ')
        for i in range(1, N+1):
            if(visited2[i] == 0 and graph[V][i]==1):
                queue.append(i)
                visited2[i] = 1

dfs(V)

bfs(V)