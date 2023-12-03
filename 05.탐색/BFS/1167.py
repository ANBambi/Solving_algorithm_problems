# baekjoon 1167번 트리의 지름
# 작성일자 : 2023-10-18 , 작성자: AN밤비

# 슈도코드

# N(노드 개수)
# A(그래프 데이터 저장 인접 리스트)

# for N만큼 반복:
#     A 인접 리스트에 그래프 데이터 저장
#     노드 번호(연결 에지 2개, 노드가 없으니 종료 -1 ) 이게 한 세트
    
# visited 리스트 초기화
# distance 리스트 초기화

# bfs:
#     큐 자료구조에 시작노드 삽입
#     visited 리스트에 현재 노드 방문 기록
#     while 큐가 비어있을때까지:
#         큐에서 노드데이터 가져오기
#         for 현재 노드의 연결 노드:
#             if 미방문 노드:
#                 큐에 데이터 삽입
#                 visited 리스트에 방문 기록
#                 큐에 삽입 된 노드 거리 = 현재 노드의 거리 + 에지의 가중치로 변경

# BFS(임의의 점 시작점) 실행
# distance 리스트에서 가장 큰 값을 지닌 노드를 시작점으로 지정
# visited 리스트 초기화
# distance 리스트 초기화

# BFS(새로운 시작점) 실행
# distance 리스트에서 가장 큰 수를 정답으로 출력

from collections import deque

N = int(input())
A = [[] for _ in range(N+1)]

for _ in range(N):
    data = list(map(int,input().split()))
    index = 0
    S = data[index]
    index += 1
    while True:
        E = data[index]
        if E == -1:
            break
        V = data[index + 1]
        A[S].append((E, V))
        index += 2
        
distance = [0] * (N+1)
visited =[False] * (N+1)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_node = queue.popleft()
        for i in A[now_node]:
            if not visited[i[0]]:
                visited[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[now_node] + i[1] # 거리 리스트 업데이트
                
bfs(1)
Max = 1

for i in range(2, N+1):
    if distance[Max] < distance[i]:
        Max = i # 거리 리스트값 중 Max값으로 시작점을 설정

distance = [0] * (N+ 1)
visited = [False] * (N+1)
bfs(Max)

distance.sort()
print(distance[N])

# from collections import deque

# V = int(input())

# graph = [[] for _ in range(V+1)]
# visited = [-1 for _ in range(V+1)]

# for _ in range(V):
#     input_data = list(map(int, input().split()))
#     head_idx = input_data[0]

#     for i in range(1, len(input_data)-2, 2):
#         tail_idx = input_data[i]
#         weight = input_data[i+1]
#         temp = (tail_idx, weight)
#         graph[head_idx].append(temp)

#         if input_data[i+2] == -1:
#             break

# def bfs(start_node):
#     que = deque()
#     que.append(start_node)
#     visited[start_node] = 0
#     max_distance, max_node = 0, 0

#     while que:
#         idx = que.popleft()

#         for next_node, w in graph[idx]:
#             if visited[next_node] == -1:
#                 que.append(next_node)
#                 visited[next_node] = visited[idx] + w

#                 if max_distance < visited[next_node]:
#                     max_distance, max_node = visited[next_node], next_node

#     return max_distance, max_node

# max_distance, max_node = bfs(1)

# print(max_distance)
    