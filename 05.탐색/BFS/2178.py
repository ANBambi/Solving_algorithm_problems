# from collections import deque

# # 2차원 배열 함수를 받아내야하는 문제인경우 습관처럼 나와야하는 것
# row, col = map(int, input().split())
# miro = [list(map(int, input().strip())) for _ in range(row)]


# # 체스처럼 움직이는 경우 움직이는 경우의 수 4가지
# move_x = [-1, 1, 0, 0]
# move_y = [0, 0, 1, -1]


# # 2차원 표를 넘어가지 않는 경우
# def valid(col, row, x, y, now):
#     if  0 <= x < col and 0 <= y < row:
#         if miro[x][y] != 0 and not visited[x][y]:
#             visited[x][y]=True
#             miro[x][y] = miro[now[0]][now[1]]+1
#             return True

# visited = [[False] * col for _ in range(row)]

# def BFS(col, row):
#     que = deque([(0, 0)])
#     visited[0][0] = True
#     result = 1

#     while que:
#         now = que.popleft()
#         for i in range(4):
#             x = now[0] + move_x[i]
#             y = now[1] + move_y[i]

#             if valid():
#                 que.append((x, y))  # 좌표로 확장
#     return result


# result = BFS(0, 0)
# print(miro[row-1][col-1])

from collections import deque

row, col = map(int, input().split())
miro = [list(map(int, input().strip())) for _ in range(row)]
visited = [[False] * col for _ in range(row)]

move_x = [-1, 1, 0, 0]
move_y = [0, 0, 1, -1]


def BFS(i, j):
    que = deque()
    que.append((i, j))
    visited[i][j] = True
    
    while que:
        now = que.popleft()

        for k in range(4):
            new_x = now[0] + move_x[k]
            new_y = now[1] + move_y[k]

            if new_x >= 0 and new_y >= 0 and new_x < row and new_y < col:
                if miro[new_x][new_y] != 0 and not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    miro[new_x][new_y] = miro[now[0]][now[1]] + 1
                    que.append((new_x, new_y))
                


BFS(0,0)
print(miro[row-1][col-1])

# from collections import deque

# # 행(row)과 열(col)의 개수를 입력 받음
# row, col = map(int, input().split())

# # 미로 정보를 2차원 리스트로 입력 받음
# miro = [list(map(int, input().strip())) for _ in range(row)]

# # 방문 여부를 나타내는 2차원 리스트 초기화
# visited = [[False] * col for _ in range(row)]

# # 상하좌우로 이동하는 방향을 정의
# move_x = [-1, 1, 0, 0]
# move_y = [0, 0, 1, -1]

# def BFS(i, j):
#     que = deque()
#     que.append((i, j))
#     visited[i][j] = True
    
#     while que:
#         now = que.popleft()

#         for k in range(4):
#             new_x = now[0] + move_x[k]
#             new_y = now[1] + move_y[k]

#             # 새로운 좌표가 유효한 범위 내에 있는지 확인
#             if 0 <= new_x < row and 0 <= new_y < col:
#                 # 벽이 아니고 아직 방문하지 않았는지 확인
#                 if miro[new_x][new_y] != 0 and not visited[new_x][new_y]:
#                     visited[new_x][new_y] = True
#                     miro[new_x][new_y] = miro[now[0]][now[1]] + 1
#                     que.append((new_x, new_y))

# # 시작점에서 BFS 시작
# BFS(0, 0)

# # 도착점의 최단 경로 출력
# print(miro[row-1][col-1])