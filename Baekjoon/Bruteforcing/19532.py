# 작성일자: 2024-05-27 MON , 작성자: 이민영
# 연립방정식 공식

# 1. 일반 풀이법
a, b, c, d, e, f = map(int, input().split())
print((c * e - b * f) // (a * e - b * d), (a * f - c * d) // (a * e - b * d))

# 2. 브루트포스 풀이법

a, b, c, d, e, f = map(int, input().split())
for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (a * i) + (b * j) == c and (d * i) + (e * j) == f:
            print(i, j)
