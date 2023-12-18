import sys

input = sys.stdin.readline

basket_n, number_m = map(int, input().split())
basket_list = [i for i in range(1, basket_n + 1)]

for _ in range(number_m):
    start, end = map(int, input().split())
    Temp = basket_list[start - 1 : end]
    Temp.reverse()
    basket_list[start - 1 : end] = Temp

    # print("(start, end) = (%d, %d). basket_n: " % (start, end), basket_list)

print(*basket_list)
