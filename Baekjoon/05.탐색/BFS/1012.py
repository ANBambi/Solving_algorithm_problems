# backjoon 1012번 유기농 배추
# 작성일자 : 2023-10-13 , 작성자 : AN밤비

# 슈도코드
# T (테스트 케이스 수)
# M(배추밭 가로길이), N(세로길이), K(배추 위치의 개수)
# Array (2차원 배열 초기화)
# result 초기화

# for - K까지 돌기:
#     x, y (배추의 위치)
#     array에 1 표시하기
    
# for M :
#     for N :
#         방문되었다면 bfs 돌게
        
        
# dn = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# bfs:
#     큐 초기화
#     글로벌 결과
#     방문한 위치 q에 append하기
#     graph 시작 위치 지정
    
#     q 만 반복:
#         x, y 를 q에서 지우기
#         4방향 값 추가해주기
#         만약 dx, dy 가 범위 안에 있고 방문했다면:
#             q에 dx, dy 삽입
#             graph의 위치를 다시 0 이라고 기준을 잡는다
#     result에 1 더해주기
    

# 결과값 출력

# Code

import sys
from collections import deque

input=sys.stdin.readline
    
dn = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def bfs(a, b):
    queue = deque()
    global result
    queue.append([a, b])
    array[a][b] = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx = x + dn[i][0]
            dy = y + dn[i][1]
            if 0 <= dx < N and 0 <= dy < M and array[dx][dy] == 1:
                queue.append([dx,dy])
                array[dx][dy] = 0
    result += 1

T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())
    array = [[0]*(M) for i in range(N)]
    result = 0
    
    for i in range(K):
        x, y = map(int,input().split())
        array[y][x] = 1

    for i in range(N):
        for j in range(M):
            if array[i][j] == 1:
                bfs(i,j)



    print(result)
    
    
    
    