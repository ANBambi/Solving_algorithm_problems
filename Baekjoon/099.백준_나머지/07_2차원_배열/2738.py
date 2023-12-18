# baekjoon 2738번 행렬덧셈
# 작성일자 : 2023-10-17 , 작성자 : AN밤비

N, M = map(int,input().split())
a = []
b = []
c = []


for i in range(N):
    A = list(map(int, input().split()))
    a.append(A)
for i in range(N):
    B = list(map(int,input().split()))
    b.append(B)
    
for i in range(N):
    for j in range(M):
        c.append(a[i][j] + b[i][j])
    print(*c)
    c.clear()
    