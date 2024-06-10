# 작성일자 : 2024-06-10 MON, 작성자 : 이민영
# 백준 2839번 설탕 배달

# BruteForcing ver.
N = int(input())
answer = 0

while N >= 0:
    if N % 5 == 0:
        answer += N // 5
        print(answer)
        break
    N -= 3
    answer += 1
else:
    print(-1)


# DP 버전
import sys

input = sys.stdin.readline


def DP(n):
    dp_list = [float("inf")] * (n + 1)
    dp_list[0] = 0

    for i in range(3, n + 1):
        dp_list[i] = min(dp_list[i - 3] + 1, dp_list[i - 5] + 1)

    if dp_list[n] == float("inf"):
        return -1
    else:
        return dp_list[n]


n = int(input())
D = DP(n)

print(D)
