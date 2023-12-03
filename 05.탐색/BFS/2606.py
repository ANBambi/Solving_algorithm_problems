# backjoon 2606번 바이러스
# 작성일자 : 2023-10-11 , 작성자: AN밤비

# 슈노코드
# computer(컴퓨터 수)
# network(네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수, for문 값)
# u, v(한 줄에 한 쌍씩 네트워크 상에서 
# graph (2차원 배열 리스트)
# count 초기화

# for network 갯수만큼
    # 입력받기
    # 양방향으로 연결 해주기

# dfs 구현
# graph, start, visited=[1]
    # 현재 노드 방문표시
    # 현재 노드와 연결된 노드 확인 for문
        # 연결된 노드 방문 / count 증가
    
# dfs 호출 결과 출력

# bfs 구현
# 큐 초기화, 시작 노드를 큐에 추가
# 시작 노드를 방문한 것으로 표시
# 큐가 빌때까지 반복
#     큐에서 노드 하나 빼오기
#      해당 노드와 연결된 노들들을 확인하며 반복:
#         만약 연결된 노드가 방문하지 않은 노드라면
#         해당 노드를 방문한 것으로 표시하고 큐에 추가
# BFS를 시작 노드로 호출, 연결된 노드 수 구하기
    
# import sys
# input = sys.stdin.readline

# computer = int(input())
# network = int(input())

# graph = [[]*computer for _ in range(computer+1)]

# count = 0

# for _ in range(network):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
        
# def dfs(graph, start, visited=[1]):
#     global count
#     visited.append(start)
#     for node in graph[start]:
#         if node not in visited:
#             count += 1
#             dfs(graph, node, visited)

#     return count

# print(dfs(graph, 1))

import sys
from collections import deque

def input():
    return sys.stdin.readline()

computer = int(input())
network = int(input())
graph = [[] for _ in range(computer + 1)]

count = 0

for _ in range(network):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(graph, start):
    visited = [False] * (len(graph))
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        for sidenode in graph[node]:
            if not visited[sidenode]:
                visited[sidenode] = True
                queue.append(sidenode)
                
    return sum(visited) - 1

print(bfs(graph, 1))