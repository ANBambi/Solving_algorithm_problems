# baekjoon 2583번 영역 구하기
# 작성 일자 : 2023-10-23 , 작성자 : AN밤비

# DFS

import sys
sys.setrecursionlimit(10000)

M, N, K = map(int,input().split())
matrix = [[0]*N for _ in range(M)]
visited = [[False]*N for _ in range(M)]

dn = [(1,0),(-1,0),(0,1),(0,-1)]

for _ in range(K):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            matrix[j][i] == 1

def DFS(x, y):
    if x < 0 or y < 0 or x >= M or y >= N:
        return 0
    
    if visited[x][y] or matrix[x][y] == 0:
        return 0
    visited[x][y] = True
    area += 1
    
    for dx, dy in dn:
        nx, ny = x + dx, y + dy
        area += DFS(nx, ny)
        
    return area
            
areas = []
for i in range(M):
    for j in range(N):
        if not visited[i][j] and matrix[i][j] == 0 :
            area = 0
            DFS(i,j)
            areas.append(area)

print(len(areas))
print(*sorted(areas))
# -----------------------------------------------------
import sys
sys.setrecursionlimit(10000)
M, N, K = map(int, input().split())
visited = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            visited[j][i] = 1

# DFS 함수 정의
def dfs(x, y):
    global area
    if x < 0 or y < 0 or x >= M or y >= N:
        return
    if visited[x][y] == 1:
        return
    visited[x][y] = 1
    area += 1
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        dfs(x + dx, y + dy)

# 각 영역의 넓이를 계산하여 저장할 리스트
areas = []

# 전체 visited를 돌면서 DFS 수행
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            area = 0
            dfs(i, j)
            areas.append(area)

# 결과 출력
print(len(areas))
print(*sorted(areas))