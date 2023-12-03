# backjoon 2667번 단지번호붙이기
# 작성일자 : 2023-10-11 , 작성자: AN밤비

# # 슈도코드
# N(지도 크기(N*N))
# array(단지 리스트)
# visited(방문체크 리스트)
# # dx(x움직인 방향)
# # dy(y움직인 방향)

# dn으로 쓸까[(0, -1), (0, 1), (-1, 0), (1, 0)] 상하좌우
# count 초기화

# # bfs 구현
# bfs:
#     큐 초기화 시작점 추가
#     방문점에 방문했음 표시
#     큐 반복:
#         큐에서 노드 꺼내기
#         카운트로 영역 크기 증가
#         방향 확인:
#             dx 꺼낸값 + 확인값
#             dy 꺼낸값 + 확인값
#             만약 범위 안에 있고:
#                 만약 방문하지 않았고, 값이 1이면 탐색:
#                     큐에 변화값 추가
#                     방문점 방문 표시
#     영역 크기 반환
# res(영역크기 저장 리스트)
# 지도 만들기(N):
#     지도 만들기(N):
#         방문하지 않았고 값이 1인 경우에 대해 탐색하기
#         영역의 크기 찾아서 리스트에 추가(반복)

# 영역 개수 출력
# 영역의 크기 오름차순 정렬
# 길이만큼 for문:
#     각 영역 크기 출력

import sys
from collections import deque
input=sys.stdin.readlines

N = int(input())
array = [str(input()) for _ in range(N)] # 단지리스트
visited = [[False for _ in range(N)] for _ in range(N)]
dn = [(0, -1), (0, 1), (-1, 0), (1, 0)] # 상, 하, 좌, 우
count = 0

def bfs(i, j):
    queue = deque([(i, j)]) # 큐 초기화, 시작점 추가
    visited[i][j] = True
    while queue:
        x, y = queue.popleft()
        count += 1
        for a, b in dn:
            dx = x + a
            dy = y + b
            if 0 <= dx < N and 0 <= dy < N:
                if visited[dx][dy] == False and array[dx][dy] == "1":
                    queue.append((dx,dy))
                    visited[dx][dy] = True
                    
    return count

reset = []
for i in range(N):
    for j in range(N):
        if visited[i][j] == False and array[i][j] == "1":
            reset.append(bfs(i, j))

print(len(reset))
reset.sort()
for i in reset:
    print(i)