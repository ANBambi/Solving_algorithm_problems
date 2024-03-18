# 작성일자 : 2024-03-18 , 작성자 : AN밤비
# 백준 1427번 소트인사이드

# 슈도코드
# A (자릿수 별로 구분해 저장한 리스트)
# A 리스트 저장

# for i 를 A 리스트 만큼 반복:
#     for j 를 i+1 ~ A 리스트 길이만큼 반복:
#         현재 범위에서 Max 값 찾기
#     현재 i의 값과 Max 값 중 Max값이 더 크면 swap 수행

import sys

print = sys.stdin.readline

A = list(input())

for i in range(len(A)):
    Max = i
    for j in range(i + 1, len(A)):
        # 내림차순이므로 최댓값 찾기
        if A[j] > A[Max]:
            Max = j
    if A[i] < A[Max]:
        temp = A[i]
        A[i] = A[Max]
        A[Max] = temp

for i in range(len(A)):
    print(A[i])
