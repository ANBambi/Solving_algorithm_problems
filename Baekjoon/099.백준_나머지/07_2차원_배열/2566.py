# baekjoon 2566 최댓값
# 작성일자 : 2023-10-17 , 작성자 : AN밤비

for i in range(9):
    a = list(map(int,input().split()))
    if i == 0:
        max_value = max(a)
        row = i + 1
        col = a.index(max_value) + 1
    else:
        if max_value < max(a):
            max_value = max(a)
            row = i + 1
            col = a.index(max_value) + 1

print(max_value)
print(row, col)