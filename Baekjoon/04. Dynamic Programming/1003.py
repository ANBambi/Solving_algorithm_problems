import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    count_0 = [1, 0]
    count_1 = [0, 1]
    N = int(input())
    if N > 1:
        for i in range(N-1):
            count_0.append(count_1[-1])
            count_1.append(count_0[-2] + count_1[-1])

    print(count_0[N], count_1[N])


# 피보나치 함수 정의
def fibonacci(n):
    if n == 0:
        return (1, 0)
    elif n == 1:
        return (0, 1)
    else:
        a, b = fibonacci(n - 1)
        c, d = fibonacci(n - 2)
        return (a + c, b + d)

# 테스트 케이스 개수 입력
T = int(input())

# 각 테스트 케이스에 대해 처리
for _ in range(T):
    N = int(input())
    result = fibonacci(N)
    print(result[0], result[1])