# 작성일자: 2023-12-19 TUE, 작성자 : AN밤비

# 약수 구하기
import sys

numberN, ordinalNumbersK = map(int, sys.stdin.readline().split())

divisorList = []

for i in range(1, numberN + 1):
    if numberN % i == 0:
        divisorList.append(i)

if divisorList and 1 <= ordinalNumbersK <= len(divisorList):
    print(divisorList[ordinalNumbersK - 1])
else:
    print(0)
