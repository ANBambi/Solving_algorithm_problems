# 작성일자 : 2024-03-20, 작성자 : AN밤비
# 백준 11004번 K번째 수
# N(숫자 갯수), K(K번째 수) A(숫자 데이터 저장 배열)
# 별도 함수 표현 부분
# 퀵 정렬 함수(시작 ,종료, K):
#     피벗 구하기 함수(시작, 종료):
#         if 피벗 == K: 종료
#         elif K < 피벗 : 퀵 정렬 수행하기(시작, 피벗 - 1, K)
#         else: 퀵 정렬 수행하기(피벗 + 1, 종료, K)
# 피벗 구하기 함수(시작, 종료):
#     데이터가 2개인 경우는 바로 비교하여 정렬
#     M(중앙값)
#     중앙값을 시작 위치와 swap
#     pivot(피벗)을 시작 위치 값 A[S]로 저장
#     i(시작점), j(종료점)
#     while i <= j :
#         피벗보다 큰 수가 나올 때까지 i 증가
#         피벗보다 작은 수가 나올 때까지 j 감소
#         찾은 i와 j 데이터를 swap
#     피벗 데이터를 나뉜 두 그룹의 경계 index 저장하기
#     경계 index 리턴

# 퀵 정렬 수행, K번째 데이터 출력

import sys

input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))


def quickSort(Start, End, K):
    global A
    if Start < End:
        pivot = partition(Start, End)
        if pivot == K:
            # K번째 수가 pivot이면 더는 구할 필요 없음
            return
        elif K < pivot:
            # K가 pivot보다 작으면 왼쪽 그룹만 정렬
            quickSort(Start, pivot - 1, K)
        else:
            # K가 pivot보다 크면 오른쪽 그룹만 정렬
            quickSort(pivot + 1, End, K)


def swap(i, j):
    global A
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def partition(Start, End):
    global A

    if Start + 1 == End:
        if A[Start] > A[End]:
            swap(Start, End)
        return End

    M = (Start + End) // 2
    swap(Start, M)
    pivot = A[Start]
    i = Start + 1
    j = End

    while i <= j:
        while pivot < A[j] and j > 0:
            j = j - 1
        while pivot > A[i] and i < len(A) - 1:
            i = i + 1
        if i <= j:
            swap(i, j)
            i = i + 1
            j = j - 1

    # i == j 피벗의 값을 양쪽으로 분리한 가운데에 오도록 설정하기
    A[Start] = A[j]
    A[j] = pivot
    return j


quickSort(0, N - 1, K - 1)
print(A[K - 1])
