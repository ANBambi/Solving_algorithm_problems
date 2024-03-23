# 작성일자 : 2024-03-23, 작성자 : 이민영
# 백준 10989번 수 정렬하기 3
# 슈도코드
# N(정렬할 수 개수)
# count(카운팅 정렬 리스트)

# for N만큼 반복:
#     count 리스트에 현재 수에 해당하는 index의 값 1 증가

# for i 는 0~10000 까지:
#     만약 count[i]의 값이 0 이 아니면:
#         해당 값만큼 i를 반복하여 출력

import sys

input = sys.stdin.readline
N = int(input())
count = [0] * 10001

for i in range(N):
    count[int(input())] += 1

for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)
