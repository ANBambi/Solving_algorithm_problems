# 작성일자 : 2024-03-17, 작성자 : AN밤비
# 1377번 버블 소트

import sys

input = sys.stdin.readline

N = int(input())
A = []

for i in range(N):
    A.append((int(input()), i))

Max = 0
sorted_A = sorted(A)

for i in range(N):
    if Max < sorted_A[i][1] - i:
        Max = sorted_A[i][1] - i

print(Max + 1)
