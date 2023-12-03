# baekjoon 2839번 설탕배달
# 작성일자 : 2023-10-27 작성자: AN밤비


import sys
input = sys.stdin.readline

def DP(n):
    dp_list = [float('inf')] * (n+1)
    dp_list[0] = 0
    
    for i in range(3, n+1):
        dp_list[i] = min(dp_list[i-3] + 1, dp_list[i-5] +1)
        
    if dp_list[n] == float('inf'):
        return -1
    else:
        return dp_list[n]
    
n = int(input())
D = DP(n)
        
print(D)
    