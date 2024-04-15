# 작성일자: 2024-04-15 MON, 작성자: 이민영
# 백준 9063번 대지
# 슈도코드
N = int(input())
xList = []
yList = []
for _ in range(N):
    x, y = map(int, input().split())
    xList.append(x)
    yList.append(y)

xLength = max(xList) - min(xList)
yLength = max(yList) - min(yList)

print(xLength * yLength)
