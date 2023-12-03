# backjoon 11725번 트리의 부모 찾기
# 작성일자 : 2023-10-16, 작성자 : AN밤비

# 슈도코드 
# 루트 : 1
# 부모노드 번호 1~N-1 까지 순서대로 출력하기

# N(노드의 개수)
# array (리스트, N+1번 돌리기)

# 범위 노드 연결

# bfs(표, 시작점, 부모리스트): 
#     큐 초기화 시작점넣어주기

#     큐 돌리기:
#         앞의 원소 가져오기
#         해당원소에 연결된 정점 조회
#         방문하지 않은 곳, 방문값을 넣어주기
#         큐에 넣어주기

# BFS 돌리기

# 값 출력
# 두번째부터 N번째까지 :
#     부모노드 i들 출력

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

visited = [False]* (N+1)
array = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int,input().rstrip().split())
    array[a].append(b)
    array[b].append(a)
    
def bfs():
    queue = deque()
    queue.append(1)
    
    while queue:
        idx = queue.popleft()
        
        for i in array[idx]:
            if not visited[i]:
                visited[i] = idx
                queue.append(i)
                
bfs()
                        
result = visited[2:]
for i in result:
    print(i)
            