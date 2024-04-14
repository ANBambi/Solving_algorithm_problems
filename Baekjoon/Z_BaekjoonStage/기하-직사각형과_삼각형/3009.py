# 작성일자: 2024-04-14 SUN, 작성자: 이민영
# 백준 3009번 네 번째 점
# 슈도코드
xList = []
yList = []
for _ in range(3):
    x, y = map(int, input().split())
    if x in xList:
        xList.remove(x)
    else:
        xList.append(x)

    if y in yList:
        yList.remove(y)
    else:
        yList.append(y)

print(xList[0], yList[0])
