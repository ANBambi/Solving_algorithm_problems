# 작성일자 : 2024-03-26 TUE, 작성자 : 이민영
# 백준 10986번 나머지 합
# 슈도 코드
# N 입력받기(수열의 개수), M 입력받기(나누어떨어져야 하는 수)
# A 입력받기(원본 수열 저장리스트)
# S 선언하기(합 배열)
# C 선언하기(같은 나머지의 인덱스를 카운트하는 리스트)
# answer 선언하기(정답 변수)

# for i 를 1~ N-1 까지:
#     S[i] = S[i-1] + A[i]

# for i 를 0~ N-1 까지:
#     # 합배열을 M으로 나눈 나머지의 값
#     remainder = S[i] % M
#     if (remainder == 0) :
#         정답을 1 증가
#     C[remainder]의 값을 1 증가

# for i 를 0~ M-1 까지:
#     C[i](i가 나머지인 인덱스의 개수)에서 2가지를 뽑는 경우의 수를 정답에 더하기
#     # C[i]개 중 2개를 뽑는 경우의 수 계산 공식 : C[i] * (C[i]-1)/2

# 결괏값 출력

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * N
C = [0] * M
S[0] = A[0]
answer = 0

for i in range(1, N):
    S[i] = S[i - 1] + A[i]

for i in range(N):
    remainder = S[i] % M
    if remainder == 0:
        answer += 1
    C[remainder] += 1

for i in range(M):
    if C[i] > 1:
        answer += C[i] * (C[i] - 1) // 2

print(answer)
