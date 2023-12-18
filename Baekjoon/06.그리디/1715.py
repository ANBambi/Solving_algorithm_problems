# backjoon 1715번 카드 정렬하기
# 작성일자 : 2023-09-27, 작성자 : AnBambi

# 슈도코드
# N(카드 묶음 개수)
# pq(우선순위 큐)

# for N만큼 반복:
#     pq(우선순위 큐)에 데이터 저장

# # 자동정렬에 따라 작은 카드 묶음 2개를 쉽게 뽑기
# while 우선순위 큐 크기가 1 이 될 때까지:
#     2개 카드 묶음을 큐에서 뽑음
#     2개 카드 묶음을 합치는 데 필요한 비교 횟수를 결과값에 더함
#     2개 카드 묶음의 합을 우선순위 큐에 다시 넣음
    
# 결괏값 출력

from queue import PriorityQueue
N = int(input())
pq = PriorityQueue()

for _ in range(N):
    date = int(input())
    pq.put(date)

data1 = 0
data2 = 0
sum = 0

while pq.qsize() > 1:
    data1 = pq.get()
    data2 = pq.get()
    temp = data1 + data2
    sum += temp
    pq.put(temp)
    
print(sum)