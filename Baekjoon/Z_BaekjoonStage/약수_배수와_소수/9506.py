# 작성일자: 2024-04-10 WED, 작성자: 이민영
# 백준 9506번 약수들의 합
# 슈도 코드
# N (숫자 입력받기)
# if 완전수라면:
#     N = 약수들의 합
# else:
#     N + "is NOT perfect"


def is_perfect_number(N):
    divisors = []

    for i in range(1, N):
        if N % i == 0:
            divisors.append(i)
    return sum(divisors) == N, divisors


while True:
    N = int(input())
    if N == -1:
        break

    is_perfect, divisors = is_perfect_number(N)

    if is_perfect:
        divisors_str = " + ".join(str(divisor) for divisor in divisors)
        print(f"{N} = {divisors_str}")
    else:
        print(f"{N} is NOT perfect")
