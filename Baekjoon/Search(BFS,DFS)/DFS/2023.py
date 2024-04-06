# 작성일자: 2024-04-05 FRI_식목일, 작성자: 이민영
# 백준 2023번 신기한 소수
# 슈도 코드
# N (자릿수)

# # 소수 구하기 함수
# for i를 2 ~ 현재 수 / 2 + 1 까지 반복:
#     if 현재 수 % i 가 0 이면:
#         return 소수가 아님

# # DFS 구현
# DFS(숫자):
#     if 자릿수 == N:
#         현재 수 출력
#     else:
#         for i를 1 ~ 9 까지 반복:
#             if i를 뒤에 붙인 새로운 수가 홀수이면서 소수일 때:
#                 # 소수 구하기 함수 사용
#                 DEF(수 * 10 + 뒤에 붙는 수) 실행

# DFS 실행(숫자 2, 3, 5, 7로 탐색 시작)

import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline
N = int(input())


def isPrime(num):
    for i in range(2, int(num / 2 + 1)):
        if num % i == 0:
            return False
    return True


def DFS(number):
    if len(str(number)) == N:
        print(number)
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue
            if isPrime(number * 10 + i):
                DFS(number * 10 + i)


DFS(2)
DFS(3)
DFS(5)
DFS(7)
