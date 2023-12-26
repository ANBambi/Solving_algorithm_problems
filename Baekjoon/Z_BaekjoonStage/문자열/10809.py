# 작성일자: 2023-12-24 SUN, 작성자: AN밤비
# 10809번 알파벳 찾기
# 슈도코드
# 입력: 단어 word (알파벳 소문자로 이루어진 문자열)

# 각 알파벳의 처음 등장 위치를 저장할 리스트 초기화
# positions = [-1] * 26

# 단어를 순회하면서 각 알파벳이 처음 등장하는 위치를 찾음
# for i = 0 to 길이(word) - 1:
#     현재 알파벳의 ASCII 코드 계산
#     index = ASCII(word[i]) - ASCII('a')

#     처음 등장한 위치인 경우에만 저장
#     만약 positions[index] == -1 이라면:
#         positions[index] = i

# 결과 출력
# for 각 알파벳의 처음 등장 위치 pos in positions:
#     pos 출력

word = input()

positions = [-1] * 26

for i in range(len(word)):
    index = ord(word[i]) - ord("a")

    if positions[index] == -1:
        positions[index] = i

for pos in positions:
    print(pos, end=" ")
