# baekjoon 7652번 나이트의 이동 BFS
# 작성일자 : 2023-10-17 , 작성자 : AN밤비

# 슈도코드
# N(테스트케이스 개수)
# I(체스판 한 변 길이)
# board{I*I 체스판 크기}
# visited(방문체크할 목록 False초기화)
# dn(방향벡터)
# count 초기화

# night(나이트가 있는 칸)
# move_night(나이트가 이동하려고 하는 칸, (x,y))

# bfs:
#     큐 초기화, 시작점 주기
#     방문점에 방문표시
#     큐 :
#         노드 꺼내기
#         count 횟수 추가
#         dx 꺼낸값 + 추가값
#         범위 안에 있고, 방문하지 않았다면:
#             queue에 변화값 추가하기
#             방문 표시하기
#     이동횟수 반환

import sys    
from collections import deque
input = sys.stdin.readline

dn = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] # 8방향

def bfs(a, b):

    while queue:
        x, y = queue.popleft()
        if x == a and y == b:
            return visited[y][x]-1
        for c, d in dn:
            ddx = x + c
            ddy = y + d
            if ddx < 0 or I <= ddx or ddy < 0 or I <= ddy:
                continue
            if not visited[ddy][ddx]:
                visited[ddy][ddx] = visited[y][x] + 1
                queue.append([ddx, ddy])
                
number = []
t = int(input())
for _ in range(t):
    I = int(input())
    x_start, y_start = map(int, input().split())
    x_move, y_move = map(int, input().split())
    
    visited = [[0]*I for _ in range(I)]
    queue = deque()
    queue.append([x_start, y_start])
    visited[y_start][x_start] = 1
    number.append(bfs(x_move, y_move))
    
for i in range(len(number)):
    print(number[i])

