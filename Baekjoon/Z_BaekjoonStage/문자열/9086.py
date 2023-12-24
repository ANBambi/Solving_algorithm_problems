# 작성일자: 2023-12-24 SUN, 작성자: AN밤비
# 9086번 문자열
# 슈도코드

# 줄 수

# (줄 수)만큼 for 문 반복 :
#     입력받을 문자열1 (리스트)

#     출력(리스트[0번째], 리스트[len(리스트)번째])

T = int(input())

for i in range(1, T + 1):
    text = input()
    print(text[0] + text[-1])
