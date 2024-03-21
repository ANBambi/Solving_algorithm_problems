# 작성일자: 2024-03-21, 작성자: AN밤비
# 백준 2751번 수 정렬하기2 (병합정렬)
# 슈도코드
# 병합정렬 구현
# 병합정렬(start, end):
#     start(시작점), end(종료점), middle(중간점)
#     # 재귀함수 형태로 구현
#     병합 정렬(start, middle)
#     병합 정렬(middle + 1, end)
#     for start ~ end + 1 까지:
#         tmp 리스트 저장
#     # 두 그룹을 병합하는 로직
#     index1 = start
#     index2 = middle + 1
#     while index1 <= 중간점 and index2 <= 종료점:
#         양쪽 그룹의 index가 가리키는 값을 비교한 후 더 작은 값을 tmp리스트에 저장하고, 선택된 데이터의 index값을 오른쪽으로 한 칸 이동
#         반복문이 끝난 후 남아있는 데이터 정리

# N (정렬할 수 개수)
# A (정렬할 리스트 선언)
# tmp (정렬할 때 잠시 사용할 임시 리스트 선언)

# for (N의 개수만큼):
#     A 리스트에 데이터 저장하기

# 병합정렬 함수 수행
# 결과값 출력k


import sys

input = sys.stdin.readline
print = sys.stdout.write


def mergeSort(start, end):
    if end - start < 1:
        return
    middle = int(start + (end - start) / 2)
    mergeSort(start, middle)
    mergeSort(middle + 1, end)
    for i in range(start, end + 1):
        tmp[i] = A[i]
    k = start
    index1 = start
    index2 = middle + 1
    while index1 <= middle and index2 <= end:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    while index1 <= middle:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= end:
        A[k] = tmp[index2]
        k += 1
        index2 += 1


N = int(input())
A = [0] * int(N + 1)
tmp = [0] * int(N + 1)

for i in range(1, N + 1):
    A[i] = int(input())

mergeSort(1, N)

for i in range(1, N + 1):
    print(str(A[i]) + "\n")
