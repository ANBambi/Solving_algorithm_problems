# 작성일자 : 2024-03-31 SUN, 작성자 : 이민영
# 백준 12891번 DNA 비밀번호 - 슬라이딩 윈도우 : 크기를 유지한 상태로 이동하면서 조건에 맞는지 탐색
# 슈도코드
# checkList(비밀번호 체크 리스트)
# myList(현재 상태 리스트)
# checkSecret(몇 개의 문자와 관련된 개수를 충족했는지 판단하는 변수)

# # 함수 선언
# myadd(문자 더하기 함수):
#     myList에 새로운 값을 더하고 조건에 따라 checkSecret 값 업데이트

# myremove(문자 빼기 함수):
#     myList에 새로운 값을 제거하고 조건에 따라 checkSecret 값 업데이트

# # 메인 코드
# S(문자열 크기), P(부분 문자열의 크기)
# A(문자열 데이터)
# checkList 데이터 받기
# checkList를 탐색하여 값이 0 인 데이터의 개수만큼 checkSecret 값 증가
# # 값이 0이라는 것은 비밀번호 개수가 이미 만족되었다는 뜻

# P 범위(0~P-1) 만큼 myList 및 checkSecret 에 적응하고, 유효한 비밀번호인지 판단

# for i를 P에서 S까지 반복:
#     j 선언(i - P)
#     # myadd, myremove 함수로 별도 구현
#     한 칸씩 이동하면서 제거되는 문자열과 새로 들어오는 문자열을 처리
#     유효한 비밀번호인지(checkSecret == 4) 판단해 결괏값을 업데이트

# 결괏값 출력

checkList = [0] * 4
myList = [0] * 4
checkSecret = 0


# 함수 정의 : 새로 들어온 문자를 처리하는 함수
def myadd(c):
    global checkList, myList, checkSecret
    if c == "A":
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1

    elif c == "C":
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1

    elif c == "G":
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == "T":
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1


# 제거되는 문자를 처리하는 함수
def myremove(c):
    global checkList, myList, checkSecret
    if c == "A":
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == "C":
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == "G":
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == "T":
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1


S, P = map(int, input().split())
result = 0
A = list(input())
checkList = list(map(int, input().split()))

for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1

# 초기 P 부분 문자열 처리 부분
for i in range(P):
    myadd(A[i])

# 4 자릿수와 관련된 크기가 모두 충족될 때 유효한 비밀번호
if checkSecret == 4:
    result += 1

for i in range(P, S):
    j = i - P
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        result += 1

print(result)
