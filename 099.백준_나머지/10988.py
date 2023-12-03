# baekjoon 10988번 팰린드롬인지 확인하기
# 작성일자: 2023-10-16 , 작성자: AN밤비

word = input()

if word[0:] == word[::-1]:
    print(1)
else:
    print(0)