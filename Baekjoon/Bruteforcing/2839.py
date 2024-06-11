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
