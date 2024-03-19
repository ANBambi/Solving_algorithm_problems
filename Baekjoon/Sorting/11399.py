# 작성일자 : 2024-03-19, 작성자 : AN밤비
# 백준 11399번 ATM
# 슈도코드
# N(사람 수)
# A(자릿수별로 구분해 저장한 리스트)
# S(A 합 배열: 각 사람이 인출을 완료하는데에 필요한 시간을 저장)

# for i 를 1~N 만큼 반복 :
#     for j 를 i-1 ~ 0 만큼 뒤에서부터 반복 :
#         현재 범위에서 삽입 위치 찾기

#     for j 를 i ~ insert_point+1 까지 뒤에서부터 반복 :
#         삽입을 위해 삽입위치에서 i 까지 데이터를 한 칸씩 뒤로 밀기

#     삽입 위치에 현재 데이터 저장

# for i 를 1 ~ N까지 반복:
#     A 리스트를 통한 합 배열 S 만들기

# S 리스트의 각 데이터의 합 출력

N = int(input())
A = list(map(int, input().split()))
S = [0] * N

for i in range(1, N):
    insert_point = i
    insert_value = A[i]
    for j in range(i - 1, -1, -1):
        if A[j] < A[i]:
            insert_point = j + 1
            break
        if j == 0:
            insert_point = 0
    for j in range(i, insert_point, -1):
        A[j] = A[j - 1]
    A[insert_point] = insert_value

S[0] = A[0]

for i in range(1, N):
    S[i] = S[i - 1] + A[i]

sum = 0

for i in range(0, N):
    sum += S[i]

print(sum)
