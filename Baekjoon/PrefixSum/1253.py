# 작성일자: 2024-03-30 SAT, 작성자 : 이민영
# 백준 1253번 좋다
# 슈도코드

import sys

input = sys.stdin.readline
N = int(input())
result = 0
A = list(map(int, input().split()))
A.sort()

for k in range(N):
    find = A[k]
    i = 0
    j = N - 1
    while i < j:
        if A[i] + A[j] == find:
            if i != k and j != k:
                result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif A[i] + A[j] < find:
            i += 1
        else:
            j -= 1

print(result)
