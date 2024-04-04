# 작성일자: 2024-04-04 THU, 작성자: 이민영
# 백준 11286번 절댓값 힙
# 슈도 코드

# N(연산 개수)
# 우선순위 큐 선언
# => 절댓값 기준으로 정렬되도록 설정
# => 단, 절댓값이 같으면 음수 우선 설정

# for N만큼 반복:
#     요청이 0일때: 큐가 비어 있으면 0, 비어있지 않으면 큐의 front 값 출력(get())
#     요청이 1일때: 새로운 데이터를 우선순위 큐에 더하기(put())

from queue import PriorityQueue
import sys

print = sys.stdout.write
input = sys.stdin.readline
N = int(input())
myQueue = PriorityQueue()

for i in range(N):
    request = int(input())
    if request == 0:
        if myQueue.empty():
            print("0\n")
        else:
            temp = myQueue.get()
            print(str((temp[1])) + "\n")
    else:
        # 절댓값을 기준으로 정렬하고 같으면 음수로 설정
        myQueue.put((abs(request), request))
