# 작성일자 : 2024-04-09 TUE, 작성자 : 이민영
# 백준 1987번 알파벳
# Python 은 불가능, PyPy3으로만 가능했음

import sys

input = sys.stdin.readline

R, C = map(int, input().split())
L = [["[" for i in range(C + 2)]]
names = {0: 1}
for i in range(R):
    tmp = list(input().rstrip())
    L.append(["["] + tmp + ["["])
L.append(["[" for i in range(C + 2)])
visited = [0 for i in range(27)]


def DFS(x, y, n):
    global answer
    if answer < n:
        answer = n

    tmp = L[x][y - 1]
    idx = ord(tmp) - 65
    if visited[idx] == 0:
        visited[idx] = 1
        DFS(x, y - 1, n + 1)
        visited[idx] = 0

    tmp = L[x][y + 1]
    idx = ord(tmp) - 65
    if visited[idx] == 0:
        visited[idx] = 1
        DFS(x, y + 1, n + 1)
        visited[idx] = 0

    tmp = L[x - 1][y]
    idx = ord(tmp) - 65
    if visited[idx] == 0:
        visited[idx] = 1
        DFS(x - 1, y, n + 1)
        visited[idx] = 0

    tmp = L[x + 1][y]
    idx = ord(tmp) - 65
    if visited[idx] == 0:
        visited[idx] = 1
        DFS(x + 1, y, n + 1)
        visited[idx] = 0


answer = 1
visited[-1] = 1
visited[ord(L[1][1]) - 65] = 1
DFS(1, 1, 1)
print(answer)
