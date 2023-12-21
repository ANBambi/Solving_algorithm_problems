# 작성일자: 2023-12-21 THU, 작성자: AN밤비
# 10815번 숫자 카드
# 슈도코드

# myCardCount(가지고 있는 카드 갯수)
# myCardList[가지고 있는 카드 입력 및 정렬]
# myCardList 정렬

# cardCheckCount(확인해야할 카드 갯수)
# cardCheckList[List로 확인할 카드들 입력받기]
# cardCheckList 정렬

# 함수 binarySearch(찾을카드, 시작인덱스, 끝인덱스):
#     while 시작인덱스 <= 끝 인덱스:
#         중간값((시작인덱스 + 끝인덱스)/2)
#         myCardList[중간값] == 찾을카드:
#             True 반환
#         그게 아니라 myCardList[중간값] < 찾을카드:
#             시작인덱스 (중간+i)
#         아니면:
#             끝인덱스 (중간-i)
#     False 반환

# # 각각 확인할 카드에 대해 이진 탐색 수행 및 결과 출력하기
# 각각 카드가 cardCheckList에 대해:
#     result = binarySearch함수()
#     결과 출력

import sys

input_func = sys.stdin.readline

myCardCount = int(input_func())
myCardList = list(map(int, input_func()).split())
myCardList.sort()

cardCheckCount = int(input_func())
cardCheckList = list(map(int, input_func()).split())
cardCheckList.sort()


def binarySearch(target, startIndex, endIndex):
    while startIndex <= endIndex:
        mid = (startIndex + endIndex) // 2
        if myCardList[mid] == target:
            return True
        elif myCardList[mid] < target:
            startIndex = mid + 1
        else:
            endIndex = mid - 1
    return False


# 각각의 확인할 카드에 대해 이진 탐색 수행 및 결과 출력
for card in cardCheckList:
    result = binarySearch(card, 0, myCardCount - 1)
    print(1 if result else 0, end=" ")
