# 작성일자 : 2024-03-13 , 작성자 : AN밤비
# 백준 1920번 수찾기

# 슈도코드
# N (수 개수)
# A (수 데이터 리스트 정렬)
# A 리스트 정렬
# M (탐색할 숫자 개수)
# targetList (탐색할 수 데이터 리스트 저장)

# for M 개수만큼 반복:
#     target(찾아야하는 수)
#     # 이진 탐색 시작
#     start(시작 인덱스)
#     end(종료 인덱스)
#     while 시작인덱스 <= 종료인덱스 :
#         midi(중간 인덱스)
#         midv(중앙값)
#         if 중앙값 > target :
#             종료 인덱스 = 중간 인덱스 - 1
#         elif 중앙값 < target :
#             시작 인덱스 = 중간 인덱스 + 1
#         else :
#             찾았음, 반복문 종료
#     if (찾았음) 1 출력
#     else 0 출력

N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
targetList = list(map(int, input().split()))

for i in range(M):
    find = False
    target = targetList[i]

    start = 0
    end = len(A) - 1
    while start <= end:
        midi = int((start + end) / 2)
        midv = A[midi]
        if midv > target:
            end = midi - 1
        elif midv < target:
            start = midi + 1
        else:
            find = True
            break
    if find:
        print(1)
    else:
        print(0)
