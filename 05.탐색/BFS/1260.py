# backjoon 1260번 DFS 와 BFS
# 작성일자 : 2023-10-11 , 작성자 : 이민영

# 슈노코드
# N 정점 번호 개수, M(간선의 개수, edge 개수), V(StartPoint, 시작점)
# A_list(그래프 데이터 저장 리스트)

# for M 개수만큼 반복:
#     A_list에 그래프 데이터 저장

# #  방문할 수 있는 노드가 여러개일때, 번호가 작은 것 먼저 방문

# for N+1 만큼 반복:
#     각 노드와 관련된 edge 결정됨

# # DFS
# DFS:
#     현재 노드 위치 출력
#     visited 리스트에 현재 노드 위치 방문 기록
#     현재 노드의 연결 노드 중 방문하지 않은 노드 DFS 실행(재귀함수)
    
#     visited 초기화
#     DFS(V)실행

# BFS
# BFS:
#     큐 자료구조에 시작노드 체크
#     visited 리스트에 현재 노드 위치 방문 기록
#     while 큐가 비어있을 때까지:
#         큐에서 노드데이터 가져오기
#         가져온 노드 출력
#         현재 노드의 연결 노드 중 방문하지 않은 노드 Queue에 삽입하기
#         visited 방문기록
#     visited 초기화
#     BFS(V) 실행

from collections import deque
N, M, V = map(int,input().split())

A_list = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int,input().split())
    A_list[s].append(e) # 인접리스트에 데이터 넣기
    A_list[e].append(s) # 인접 리스트 데이터 넣기

# 방문할 수 있는 노드가 여러개일 경우, 작은 번호부터 먼저 방문해야함.

for i in range(1, N+1):
    A_list[i].sort() # 번호가 작은 노드부터 방문하기 위해 정렬

# DFS 구현
def DFS(v):
    print(v, end='')
    visited[v] = True
    for i in A_list[v]:
        if not visited[i]:
            DFS(i)
            
visited = [False] * (N+1)
DFS(V)

# BFS 구현
def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v]=True
    while queue:
        now_node = queue.popleft()
        print(now_node, end='')
        
        for i in A_list[now_node]:
            if not visited[i]:
                visited[i]=True
                queue.append(i)

print()
visited = [False] * (N+1)
BFS(V)
    