# 백준 1158번 문제풀이 작성자 AN밤비

# n, k = map(int, input().split())
# circle = [str(i+1) for i in range(n)]
# out = []
# for i in range(n):
#     out.append(circle[(k-1) % len(circle)])
#     circle = circle[(k-1) % len(circle)+1:]+circle[:(k-1) % len(circle)]
# print('<'+', '.join(out)+'>')

import sys

n, k = map(int, sys.stdin.readline().split())

arr = [i+1 for i in range(n)]
ans = []
num = 0

while arr:
    num += k-1
    if num >= len(arr):
        num = num % len(arr)

    ans.append(str(arr.pop(num)))

answer = ", ".join(ans)
print(f"<{answer}>")
