# baekjoon 2563번 색종이
# 작성일자 : 2023-10-17 , 작성자 : AN밤비

paper = [[0 for j in range(100)] for i in range(100)]
count = 0

N = int(input())
for i in range(N):
    x, y = list(map(int, input().split()))
    for x_idx in range(x, x+10):
        for y_idx in range(y, y+10):
            paper[x_idx][y_idx] = 1
            
for row in paper:
    count += row.count(1)
    
print(count)