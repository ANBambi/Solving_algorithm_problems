# 작성일자 : 2024-03-28 THU, 작성자 : 이민영
# 백준 2018번 수들의 합 5
# 슈도코드
# N (변수 저장)
# 사용변수 초기화

# while end_index != N:
#     if sum == N : 경우의 수 증가, end_index 증가, sum 값 반영
#     elif sum > N : sum 값 변경, start_index 증가,
#     else: end_index 증가, sum 값 변경

# 경우의 수 출력

N = int(input())
count = 1
start_index = 1
end_index = 1
sum = 1

while end_index != N:
    if sum == N:
        count += 1
        end_index += 1
        sum += end_index
    elif sum > N:
        sum -= start_index
        start_index += 1
    else:
        end_index += 1
        sum += end_index

print(count)
