# 작성일자 : 2024-06-11 TUE, 작성자 : 이민영
# 백준 2587번 대표값2

# 슈도코드
# 리스트에 숫자 저장(총 5회반복)
# 평균 구하기
# 리스트 정렬
# 중간값 구하기

num_list = []

for i in range(5):
    num_list.append(int(input().strip()))

average = sum(num_list) // 5

num_list.sort()
median = num_list[2]

print(average)
print(median)
