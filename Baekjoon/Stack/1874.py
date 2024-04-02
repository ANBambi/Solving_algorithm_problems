# 작성일자: 2024-04-02 TUE, 작성자: 이민영
# 백준 1874번 스택 수열
# 슈도코드
# N (수열개수) A(수열 리스트)
# A (수열 리스트 채우기)

# for N만큼 반복:
#     if 현재 수열값 >= 오름차순 자연수:
#         while 현재 수열값 >= 오름차순 자연수:
#             append()
#             오름차순 자연수 1 증가
#             (+) 저장
#         pop()
#         (-) 저장
#     else 현재 수열값 < 오름차순 자연수:
#         pop()
#         if 스택 pop 결과값 > 수열의 수:
#             NO 출력
#         else:
#             (-)저장

# if NO 값을 출력한 적 없으면:
#     저장한 값 출력

import sys

input = sys.stdin.readline

N = int(input())
A = [0] * N

for i in range(N):
    A[i] = int(input())

stack = []
num = 1
result = True
answer = ""

for i in range(N):
    su = A[i]
    if su >= num:
        while su >= num:
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else:
        n = stack.pop()
        if n > su:
            print("NO")
            result = False
            break
        else:
            answer += "-\n"

if result:
    print(answer)
