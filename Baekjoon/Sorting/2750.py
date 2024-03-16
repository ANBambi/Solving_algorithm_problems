# 작성일자 : 2024-03-16, 작성자 : AN밤비
# 백준 2750번 수 정렬하기 (버블정렬)
# 슈도코드
# N (정렬할 수 개수)
# A (수 저장 리스트 선언, 입력데이터 저장)

# for i 를 0 ~ N-1 만큼 반복
#     for j 를 0 ~ N-1-i 만큼 반복
#         현재 A 리스트의 값보다 1칸 오른쪽 리스트의 값이 더 작으면 두 수 바꾸기

# A 리스트 출력(한 줄씩)

N = int(input())
A = [0] * N

for i in range(N):
    A[i] = int(input())

for i in range(N - 1):
    for j in range(N - 1 - i):
        if A[j] > A[j + 1]:
            temp = A[j]
            A[j] = A[j + 1]
            A[j + 1] = temp

for i in range(N):
    print(A[i])
