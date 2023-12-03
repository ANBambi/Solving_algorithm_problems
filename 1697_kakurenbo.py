# 1697번 숨바꼭질
# 2023-08-27 AN

from collections import deque

# 입력값 받기
n, k = map(int,input().split())
# 움직일 수 있는 최대 좌표는 100000
max_num = 10**5
visited = [0] * (max_num +1)

# bfs 함수 정의
def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        # 수빈이 위치가 동생의 위치와 같다면 반복문 종료
        if x == k:
            print(visited[x])
            break
        # 이동할 수 있는 방향에 대해
        for j in (x-1, x+1, x*2):
            # 주어진 범위 내에 있고 아직 방문하지 않았다면
            if 0 <= j <= max_num and not visited[j]:
                # 이동한 위치에 현재 이동한 시간 표시 // index 값, 단계 값
                visited[j] = visited[x] + 1
                q.append(j)

# bfs 실행
bfs()