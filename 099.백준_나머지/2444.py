# backjoon 2444번 별찍기 - 7
# 작성일자 : 2023-10-14 , 작성자 : AN밤비

# 2N - 1 번째까지 별 출력한다.

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
# n = int(input())

# for i in range(1, n+1):
#     print(' ' * (n-i) + '*' * (2*i -1))
    
# for i in range(1, n):
#     print(' ' * i + '*' * (2*(n-i) -1))


n = int(input())

for i in range(1, n):
    blank = " " * (n - i)
    star = "*" * (2*i - 1)

    print(blank + star)

print("*"*(2*n-1))

for i in range(n-1, 0, -1):
    blank = " " * (n - i)
    star = "*" * (2*i - 1)

    print(blank + star)
