# backjoon 10026번 적록색약 dfs.ver
# 작성일자 : 2023-10-14 , 작성자: AN밤비

# 슈도코드

# 재귀함수 호출횟수 설정
# N(그리드의 가로, 세로 개수)
# graph(N개의 그림, N*N)
# dn 한 줄(튜플형식)

# dfs:
    # 큐 초기화
    # 큐에서 값추가
    # 방문한 곳 표시
    
    # 반복할 것:
    #     큐에서 노드꺼내기
    #     dn까지 dx dy 돌리기:
    #         vx vy에 x+dx y+dy 입력
            
    #         범위 안, 방문 안한 경우:
    #             같은색이면
    #             True표시

# 적록색약이 아닌 사람이 봤을 때의 구역의 개수
# a 초기화
# visited(방문확인할 2차원배열)

# 작업할 구역:
#     만들기 :
#         아직 방문안했다면:
#             bfs 사용하기
#             a 에 값 추가

# 적록색약인 사람이 봤을때의 구역의 수
# b 초기화
# visited(방문확인용 2차원배열)

# 작업할 구역:
#     만들기 :
#         그린 = 레드 라면
        
# 작업할 구역:
#     다시만들기:
#         방문안했으면:
#             bfs 돌리기
#             b에 값추가
    
# a, b 출력

import sys
from collections import deque

N = int(input())
graph = [list(input()) for _ in range(N)]
dn = [(0, -1),(0, 1), (1, 0),(-1, 0)]

def dfs(x, y, visited):
    visited[x][y] = True
    x, y = queue.popleft()
    for dx, dy in dn:
        vx, vy = x+dx, y+dy
            
        if 0 <= vx < N and 0 <= vy < N and visited[vx][vy] == False:
            if graph[vx][vy] == graph[x][y]:
                visited[vx][vy] = True
                queue.append((vx, vy))

# 적록색약이 아닌 경우    
a = 0
visited = [[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            bfs(i,j,visited)
            a += 1

# 적록색약인 경우
b = 0
visited = [[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G' : graph[i][j] = 'R'
        
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            bfs(i,j, visited)
            b += 1

print(a, b)