# baekjoon 2468번 안전 영역
# 작성 일자 : 2023-10-23 , 작성자 : AN밤비

# 슈도코드
# N (2차원 배열의 행과 열을 나타내는수)
# list_A 초기화
# visited 초기화


# DFS:
#     visited 리스트에 현재 노드 방문 기록
#     현재 연결된 노드중 방문하지 않은 노드 DFS 실행, 재귀함수

# for 2부터 N까지:
#     a .split 으로 띄워서 리스트로 저장

# for n까지:
#     if 방문하지 않은 노드가 있으면:
#         연결 요소 갯수 1 증가
#         DFS 실행

# 연결 요소 개수 값 입력

import sys
input = sys.stdin.readline
stack = []
max_list = []
n = int(input())
stack.append([False for k in range(n+1)])
for _ in range(n):
    p = list(map(int, input().split()))
    max_list.append(max(p))
    stack.append([0] + p + [0])
stack.append([False for k in range(n+1)])
real_max = max(max_list)

def dfs(x, y, h):
    visited = [[0 for i in range(n+1)] for i in range(n+1)]
    global stack
    root = [[x, y]]
    dn = [(1,0), (-1,0), (0,1),(0, -1)]
    while root :
        node = root.pop(-1)
        if visited[node[0]][node[1]] ==0:
            visited[node[0]][node[1]] = 1
            for p in range(0,4):
                if stack[node[(0,1)]+dn[p]] > h:
                    root.append([node[(0,1)]+dn[p]])
    return 1

r_result = 0
for i in range(real_max):
    result = 0
    visited = [[0 for i in range(n+1)] for i in range(n+1)]
    for x in range(1, n+1):
        for y in range(1, n+1):
            if visited[x][y] == 0 and stack[x][y]>i :
                result += dfs(x,y,i)
    if r_result < result:
        r_result = result
        
print(r_result)
