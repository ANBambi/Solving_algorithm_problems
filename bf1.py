# 백준 치킨치킨치킨
# 2023-07-12 이민영


from itertools import combinations
import sys

# N(사람인원 수)과 M(치킨 종류 개수)를 입력받는다.
N, M = map(int,input().split())

# 치킨 선호도 리스트
priority_list = []
# chicken = [1, 2, 3, 4, 5, ...] 같은 리스트 만들기
# 사람의 수인 N만큼 실행
for i in range(N):
    # 사람마다의 각 치킨에 대한 선호도
    priority_list.append(list(map(int, input().split())))

# print(priority_list) # 한 번 출력해보기

# -------------------------------입력 부분 끝 -------------

# 3가지 치킨을 선택하는 모든 경우의 수

comb = list(combinations(range(M), 3))

total_score_list = []
for i, j, k in comb: # 각 조합.
    
    total_score = 0
    
    # 결과 값
    for l in range(N):
        total_score += max(priority_list[l][i], priority_list[l][j], priority_list[l][k])
    total_score_list.append(total_score)
    
print(max(total_score_list))