# 작성일자: 2024-04-13 SAT, 작성자: 이민영

x, y, w, h = map(int, input().split())
print(min(x, y, w - x, h - y))
