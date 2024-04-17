# 작성일자: 2024-04-18 WED, 작성자: 이민영
# 백준 14215번 세 막대

A = list(map(int, input().split()))
A.sort()
if A[0] + A[1] > A[2]:
    print(sum(A))

else:
    print((A[0] + A[1]) * 2 - 1)
