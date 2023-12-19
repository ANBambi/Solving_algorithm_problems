import sys

input = sys.stdin.readline

theNumber = int(input())
subjectScoreList = list(map(int, input().split()))

maximum = max(subjectScoreList)

ave = sum(subjectScoreList) * 100 / (theNumber * maximum)
print(ave)

# average = 원래평균구하는 법(전체합 / 개수) * (100 / 최댓값(maximum))
