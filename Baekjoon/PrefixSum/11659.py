# 작성일자 : 2024-03-24, 작성자 : 이민영
# 백준 11659번 구간 합 구하기4
# 슈도코드
# suNo(숫자 개수), quizNo(질의 개수)
# numbers 변수에 숫자 데이터 저장
# prefix_sum 합 배열 변수 선언
# temp 변수 선언

# for 저장한 숫자 데이터 차례대로 검색:
#     temp 에 현재 숫자 데이터 더해 주기
#     합 배열에 temp값 저장

# for 질의 개수만큼 반복:
#     질의 범위 받기(start ~ end)
#     구간 합 출력하기(prefix_sum[end] - prefix_sum[start-1])

import sys

input = sys.stdin.readline
suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)

for i in range(quizNo):
    start, end = map(int, input().split())
    print(prefix_sum[end] - prefix_sum[start - 1])
