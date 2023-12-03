# baekjoon 2775번 부녀회장이 될테야
# 작성일자 : 2023-10-27, 작성자 : AN밤비

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    a_list = [[i for i in range(1, 15)] for _ in range(k + 1)]
    
    i = 0 ; j = 0
    
    while True:
        j += 1
        
        if i == 0:  # 0층일 경우 별도 처리
            a_list[i][j-1] = j
        else:
            a_list[i][j-1] = sum(a_list[i-1][:j])
        
        if i == k and j == n:
            print(a_list[i][j-1])
            break
        
        if j == 14:
            i += 1
            j = 0
    


# from sys import stdin

# t = int(stdin.readline())  # 테스트 케이스의 수 입력
# cnt = 0

# while cnt < t:
#     k = int(stdin.readline())  # 층 수 입력
#     n = int(stdin.readline())  # 호 수 입력
#     array = [t for t in range(1, n+1)]  # 초기 거주민 수 리스트 생성

#     # 각 층마다 거주민 수를 업데이트
#     for i in range(k):
#         for j in range(1, n):
#             array[j] += array[j-1]
    
#     print(array[-1])  # 마지막 호의 거주민 수 출력
#     cnt += 1