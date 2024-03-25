# 작성일자 : 2024-03-25, 작성자 : 이민영
# 백준 11660번 구간 합 구하기 5
# 슈도 코드

# N(리스트 크기), M(질의 수)
# A(원본 리스트), D(합 배열)

# for n만큼 반복:
#     원본 리스트 데이터 저장

# for i를 1 부터 n까지 반복:
#     for j를 1 부터 n까지 반복:
#         합 배열 저장
#         D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j];

# for m만큼 반복:
#     질의에 대한 결과 계산 및 출력
#     결과 = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
A = [[0] * (N + 1)]
D = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        D[i][j] = D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 1] + A[i][j]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    # 구간 합 배열로 질의에 답변
    result = D[x2][y2] - D[x1 - 1][y2] - D[x2][y1 - 1] + D[x1 - 1][y1 - 1]
    print(result)
