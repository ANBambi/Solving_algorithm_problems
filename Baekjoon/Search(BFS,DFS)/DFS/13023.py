# 작성일자: 2024-04-08 MON, 작성자: 이민영
# 백준 13023번 ABCDE
# 슈도코드

# N(노드 개수) M(에지 개수)
# A(그래프 데이터 저장 인접 리스트)
# visited(방문 기록 저장 리스트)
# arrive(도착 확인 변수)

# # DFS 구현
# DFS(현재 노드, 깊이):
#     if 깊이가 5:
#         arrive = true;
#         함수 종료
#     방문 리스트에 현재 노드 방문 기록
#     현재 노드의 연결 노드 중 방문하지 않은 노드로 DFS 실행

# for M 의 개수만큼 반복:
#     A 인접 리스트에 그래프 데이터 저장

# for N 의 개수만큼 반복:
#     노드마다 DFS 실행
#     if(arrive) 반복문 종료

# if arrive : 1 출력
# else: 0 출력

import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline
N, M = map(int, input().split())
arrive = False
A = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)


def DFS(now, depth):
    global arrive
    if depth == 5:
        arrive = True
        return
    visited[now] = True
    for i in A[now]:
        if not visited[i]:
            DFS(i, depth + 1)
    visited[now] = False


for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(N):
    DFS(i, 1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)
