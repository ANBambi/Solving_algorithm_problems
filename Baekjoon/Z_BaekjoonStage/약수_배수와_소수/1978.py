# 작성일자: 2024-04-10 WED, 작성자: 이민영
# 백준 1978번 소수 찾기
# 슈도 코드

N = int(input())
prime_number = 0
numbers = list(map(int, input().split()))


def isPrime(Number):
    for i in range(2, int(Number / 2 + 1)):
        if Number % i == 0:
            return False
    return True


for i in range(N):
    if isPrime(numbers[i]) and numbers[i] != 1:
        prime_number += 1

print(prime_number)
