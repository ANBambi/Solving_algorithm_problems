# 작성일자: 2024-03-29 FRI, 작성자 : 이민영
# 백준 1940번 주몽
# 슈도코드
# N (재료의 개수), M(갑옷이 되는 번호)
# A(재료 데이터 저장 리스트)
# A 리스트 정렬하기
# i(시작 인덱스 = 0
# j(종료 인덱스 = N -1)
# count (정답값 = 0)

# while i < j :
#     if 재료 합 < M: 작은 번호 재료를 한 칸 위로 변경
#     elif 재료 합 > M : 큰 번호 재료를 한 칸 아래로 변경
#     else 경우의 수 증가 , 양쪽 index 각각 변경

# count 출력

import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
A = list(map(int, input().split()))
A.sort()
count = 0
i = 0
j = N - 1

while i < j:
    if A[i] + A[j] < M:
        i += 1
    elif A[i] + A[j] > M:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1

print(count)
