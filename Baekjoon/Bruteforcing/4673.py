# 작성일자: 2023-12-20 WED, 작성자: AN밤비
# 4673번 셀프 넘버
# 슈도코드

# 함수 decompostion(n) 분해합함수:
#     반환 n + 각 자릿수 합

# 함수 selfNumbers():
#     상한값은 10000까지만
#     numbers = 1부터 상한값까지 숫자 집합
#     gengeratedNumbers = 빈 집합

#     반복문 i를 1부터 상한값까지:
#         generatedNumbers에 decomposition(i)를 추가 (이러면 분해합이 들어감)

#     selfNumbers는 numbers에서 generatedNumbers 뺀 값 (이러면 전체 - 분해합 = 셀프넘버 되시겠습니다)
#     selfNumbers 정렬

# 함수 main():
#     결과 = selfNumber()
#     각각의 넘버에 대해서:
#         넘버를 출력


def decompostion(n):
    return n + sum(map(int, str(n)))


def selfNumbers():
    limit = 10000
    numbers = set(range(1, limit + 1))
    generatedNumbers = set()

    for i in range(1, limit + 1):
        generatedNumbers.add(decompostion(i))

    selfNumbers = numbers - generatedNumbers

    return sorted(list(selfNumbers))


def main():
    result = selfNumbers()
    for num in result:
        print(num)


if __name__ == "__main__":
    main()
