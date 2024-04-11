# 작성일자: 2024-04-11 THU, 작성자: 이민영
# 백준 2581번 소수
# 슈도코드

# M (이상값)
# N (이하값)
# 소수값 = []

# isPrime(현재값):
#     for i를 M부터 N+1 까지 돌리기:
#         for j를 2부터 현재값 / 2 + 1 까지 돌리기:
#             만약 현재값 약수면:
#                 소수값.append(현재값)
#                 땡
#         아니면 1

# print(sum(소수값))
# print(min(소수값))

import sys

input = sys.stdin.readline

M = int(input())
N = int(input())
primeList = []


def isPrime(Number):
    if Number < 2:
        return False
    for j in range(2, int(Number / 2 + 1)):
        if Number % j == 0:
            return False
    return True


for i in range(M, N + 1):
    if isPrime(i):
        primeList.append(i)

if primeList:
    print(sum(primeList))
    print(min(primeList))
else:
    print(-1)
