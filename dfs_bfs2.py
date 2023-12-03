from collections import deque
import sys
read = sys.stdin.readline # 너무 길어서 대체

N, M, V = map(int,read().split()) # 입력받는 수

graph = [[0] * (N+1) for _ in range(N+1)] # 그래프 구상
visited1 = [0] * (N+1) # 입력값으로 초기화_bfs용
visited2 = [0] * (N+1) # 입력값으로 초기화_dfs용

for _ in range(M):
    a, b = map(int,read().split()) # 각 점들을 입력 받아서
    graph[a][b] = graph[b][a] = 1 # 두 점이 연결되어있으니 반대방향 생각하기

def bfs(V): # 너비우선탐색
    queue = deque() # 지나갈 길 확인하기
    queue.append(V) # 지나가는거 추가
    visited1[V] = 1 # 지나갔으면 1 표시
    while queue:
        V = queue.popleft() # 맨 앞(사용된) 원소제거
        print(V, end=' ')
        for i in range(1, N+1): # N+1 까지 돌리기
            # 1과 연결된 노드 중에 방문한 적 없는  찾기
            if visited1[i] == 0 and graph[V][i] == 1: 
                queue.append(i) # 추가하기
                # 방문 1로 처리
                visited1[i] = 1
                
def dfs(V):
    # 방문 1로 처리
    visited2[V] = 1
    # 방문한 노드 출력하기
    print(V, end=' ')
    for i in range(1, N+1):
        # 1과 연결된 노드 중 방문한 적 없는 곳 찾기
        if visited2[i] == 0 and graph[V][i] == 1:
            dfs(i)
        
dfs(V)
print()
bfs(V)