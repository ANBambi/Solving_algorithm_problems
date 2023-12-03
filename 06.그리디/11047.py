# backjoon 11047번 동전 0

# 슈도코드
# N(동전 개수) K(목표 금액)
# A(동전 데이터 리스트)

# for N만큼 반복:
#     A 리스트 저장
    
# # 값이 큰 동전부터 선택해야 갯수를 최소로 구성할 수 있음
# for N만큼 반복 -> N-1 ~ 0 으로 역순으로 반복:
#     if 현재 K보다 동전가치가 작거나 같으면:
#         동전 수 += 목표 금액 / 현재 동전 가치
#         목표 금액 = 목표 금액 % 현재 동전 가치
    
# 누적된 동전 수 출력

N, K = map(int, input().split())
A = [0] * N

for i in range(N):
    A[i] = int(input())

count = 0
# 값이 큰 동전부터 선택해야 갯수를 최소로 구성할 수 있음
for i in range(N-1, -1, -1):
    if A[i] <= K:
        count += int(K / A[i])
        K = K % A[i]

print(count)