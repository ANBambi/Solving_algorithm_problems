import sys
from itertools import permutations  # 

n = int(input())
guess_list = []
for i in range(n):
    guess_list.append(list(map(int, sys.stdin.readline().split())))
    
items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number_list = list(permutations(items, 3))

# 1
for idx, i in enumerate(number_list):
    number_list[idx] = list(i)

# 2
number_list = [list(x) for x in number_list]

# 3
number_list = list(map(lambda x:list(x), number_list))

success_number = []

for i in guess_list: # [123, 1, 1]
    number = i[0]
    strike = i[1]
    ball = i[2]
    string_number = str(number)
    first_number = int(string_number[0])
    second_number = int(string_number[1])
    third_number = int(string_number[2])

    for idx, (j, k, l) in enumerate(number_list):
        s = 0
        b = 0
        if j != 0: # 탈락하지 않은 숫자
            if j == first_number: # s인지 검사
                s += 1
            else: # b인지 검사
                if str(j) in string_number:
                    b += 1
            if k == second_number: # s인지 검사
                s += 1
            else: # b인지 검사
                if str(k) in string_number:
                    b += 1
            if l == third_number: # s인지 검사
                s += 1
            else: # b인지 검사
                if str(l) in string_number:
                    b += 1
            if s == strike and b == ball: # 힌트가 일치한 숫자
                pass
            else: # 숫자를 탈락
                number_list[idx][0] = 0

cnt = 0
for j, k, l in number_list:
    if j != 0:
        cnt +=1

print(cnt)
        
    