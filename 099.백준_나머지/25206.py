# baekjoon 25026번 너의 평점은
# 작성일자 : 2023-10-16 , 작성자 : AN밤비

# 입력
import sys
input = sys.stdin.readline
data_dict = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
result = 0
total = 0

for _ in range(0, 20):
    input_data = input().split()
    
    if input_data[2] == "P":
        continue
    
    total += float(input_data[1]) # 학점 다 더하기(소수점)
    result += float(input_data[1]) * data_dict[input_data[2]] # 등급 기준 학점 찾아서 곱하기
    
grand_point_avg = result / total

conversion = format(grand_point_avg, '.6f') # 소수점 아래 6번째 자리까지 나타내기

print(conversion)