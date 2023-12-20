# 작성일자: 2023-12-20 WED, 작성자: AN밤비
# 2231번 분해합
# N의 분해합 = N과 N을 이루는 각 자릿수의 합, ex) N = 288 , 분해합 M = 288 + 2 + 8 + 8 = 306
# 분해합 N <= M

# 슈도코드
# decompositionCombination(분해합)

# for decompositionCombination까지 :
#     digitsum 공식
#     만약, digitSum이 decompositionCombination 과 같다면:
#         i가 몇인지 출력
#         멈추기

# 아니라면:
#     0 출력


decompositionCombination = int(input())
for decomposition in range(
    max(1, decompositionCombination - 54), decompositionCombination
):
    if sum(map(int, str(decomposition))) + decomposition == decompositionCombination:
        print(decomposition)
        exit(0)
print(0)
