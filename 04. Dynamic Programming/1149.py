import sys
input = sys.stdin.readline

N = int(input()) # 집
cost = [list(map(int, input().split())) for _ in range(N)] # 빨초파 칠하는 비용 리스트저장

dp = [[0] * 3 for _ in range(N)] #2차원
dp[0] = cost[0] # 초기비용

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0] # 현재집 빨강색 비용
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1] # 현재집 초록색 비용
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2] # 현재집 파랑색 비용
    
result = min(dp[N-1]) # 마지막 집 칠하는데 드는 최솟값
print(result)