n = int(input())
li = list(map(int, input().split()))

# 왼쪽에서 오른쪽으로 큰 값까지의 길이 탐색
dp_L = [1]*(n+1)
for i in range(n):
    for j in range(i):
        if li[i] > li[j]:
            dp_L[i] = max(dp_L[i], dp_L[j] + 1)

# 오른쪽에서 왼쪽으로 큰 값까지의 길이 탐색
dp_R = [1]*(n+1)
for i in reversed(range(n)):
    for j in range(n-1, i, -1):
        if li[i] > li[j]:
            dp_R[i] = max(dp_R[i], dp_R[j] + 1)

dp = [dp_L[i] + dp_R[i] for i in range(n)]
result = max(dp)-1
print(result)