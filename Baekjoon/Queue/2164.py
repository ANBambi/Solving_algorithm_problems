# 작성일자 : 2024-04-04 THU, 작성자: 이민영
# 백준 2164번 카드2
# 슈도 코드
# N(카드 개수) myQueue(카드 저장 큐)

# for 카드 개수만큼 반복:
#     큐에 카드 저장

# while 카드가 1장 남을때까지:
#     맨 위의 카드를 버림: popleft()
#     맨 위의 카드를 가장 아래 카드 밑으로 이동 : popleft() --> append()

# 마지막으로 남은 카드 출력

from collections import deque

N = int(input())
myQueue = deque()

for i in range(1, N + 1):
    myQueue.append(i)

while len(myQueue) > 1:
    myQueue.popleft()
    myQueue.append(myQueue.popleft())

print(myQueue[0])
