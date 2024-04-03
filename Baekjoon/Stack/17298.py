# 작성일자: 2024-04-03 WED, 작성자: 이민영
# 백준 17298번 오큰수
# 슈도 코드
# N(수열개수) A (수열리스트) ans(정답 리스트)
# A 수열 리스트 채우기
# myStack (스택 선언)

# for i 를 N만큼 반복:
#     while 스택이 비지 않고, 현재 수열값이 top에 해당하는 수열보다 클 때까지:
#         스택에서 pop 한 값을 index로 하는 정답 리스트 부분을 수열 리스트의 현재 값(A[i])으로 지정
#     스택에 i의 값을 저장

# while 스택이 빌 때까지:
#     스택에 있는 index의 정답 리스트에 -1 저장

# 정답 리스트 출력

import sys

input = sys.stdin.readline

N = int(input().strip())
ans = [0] * N
A = list(map(int, input().strip().split()))
myStack = []

for i in range(N):
    # 스택이 비어있지 않고 현재 수열이 스택 top인덱스가 가리키는 수열보다 클 경우
    while myStack and A[myStack[-1]] < A[i]:
        # 정답 리스트에 오큰수를 현재 수열로 저장하기
        ans[myStack.pop()] = A[i]
    myStack.append(i)

# 반복문을 다 돌고 나왔는데 스택이 비어있지 않다면 빌 때까지
while myStack:
    # 스택에 쌓인 index에 -1을 넣기
    ans[myStack.pop()] = -1

result = " ".join(map(str, ans))
print(result)
