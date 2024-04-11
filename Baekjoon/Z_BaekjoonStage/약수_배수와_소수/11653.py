# 작성일자: 2024-04-11 THU, 작성자: 이민영
# 백준 11653번 소인수분해
# 슈도코드
# N(소인수분해할 숫자)
# primeList(소인수목록)

# isPrime(현재값):
#     만약 현재값이 가장 작은 소수라면:
#         나눈 값을 값 소인수목록에 저장하고 종료
#     아니라면:
#         현재값 갱신해서 다시 소수로 나누기

# 만약 소인수목록[i]가 1이라면:
#     print("")
# 아니라면:
#     for i를 소인수목록만큼:
#         print(소인수목록[i])

import sys

input = sys.stdin.readline


def factorize(N):
    primeList = []
    current = 2
    while N > 1:
        while N % current == 0:
            N //= current
            primeList.append(current)
        current += 1
    return primeList


def printPrimes(primeList):
    if len(primeList) == 0:
        print("")
    else:
        for prime in primeList:
            print(prime)


N = int(input())
primeList = factorize(N)
printPrimes(primeList)
