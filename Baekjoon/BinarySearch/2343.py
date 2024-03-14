# 작성일자 : 2024-03-14, 작성자 : AN밤비
# 백준 2343번 기타레슨
# 슈도코드
# N, M (레슨 수, 블루레이 개수)
# A (기타 레슨 데이터 저장리스트)
# start (시작 인덱스)
# end (종료 인덱스)

# for A 리스트 탐색:
#     시작 인덱스 저장 (A 리스트 최댓값)
#     종료 인덱스 저장 (A 리스트 총합)

# while 시작 인덱스 <= 종료 인덱스:
#     middle (중간 인덱스)
#     sum (레슨합)
#     count (현재 사용한 블루레이의 갯수)

#     for N 만큼 반복:
#         if sum + 현재 레슨 시간 > 중간 인덱스:
#             count += 1
#             sum = 0
#         sum 에 현재 레슨 시간 값 더하기
#     sum 이 0 이 아니라면 마지막 블루레이 필요(count에 1 더하기)

#     if count > M :
#         시작 인덱스 = 중앙 인덱스 + 1
#     else:
#         종료 인덱스 = 중앙 인덱스 - 1

# 시작인덱스 출력


N, M = map(int, input().split())
A = list(map(int, input().split()))
start = 0
end = 0

for i in A:
    # 레슨 최댓값을 시작인덱스로 저장
    if start < i:
        start = i
    end += i

while start <= end:
    middle = int((start + end) / 2)
    sum = 0
    count = 0
    for i in range(N):
        # 중간 값으로 모든 레슨을 저장할 수 있는지 확인
        if sum + A[i] > middle:
            count += 1
            sum = 0
        sum += A[i]
    if sum != 0:
        count += 1
    if count > M:
        start = middle + 1
    else:
        end = middle - 1
print(start)
