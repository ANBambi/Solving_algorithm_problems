# 작성일자 : 2023-12-27 WED, 작성자 : AN밤비
# 2908번 상수

A, B = list(map(str, input().split()))

aList = int(A[::-1])
bList = int(B[::-1])

if aList <= bList:
    print(bList)
else:
    print(aList)
