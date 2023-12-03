# baekjoon 10798번 세로읽기
# 작성일자 : 2023-10-17 , 작성자 : AN밤비
# T = []
# Max = 0
# answer = ''

# for _ in range(5):
#     T.append(list(input()))
# for i in range(5):
#     if Max > len(T[i]):
#         Max = len(T[i])
        
# for i in range(Max):
#     for j in range(5):
#         try:
#             answer += T[j][i]
#         except IndexError:
#             pass
#         print(T[i])
        
# 5 줄에 걸쳐 입력 받기
s = [input() for i in range(5)]

        # i 번째 줄 세로로 읽기
for i in range(15):

    # j 번째 행 불러오기
    for j in range(5):

        # j 번째 행이 i 번째 글자가 있는가?
        if len(s[j]) > i:

             # 출력할 때, end 입력하면 다음 줄로 건너뛰지 않음.
             print(s[j][i], end = '')
