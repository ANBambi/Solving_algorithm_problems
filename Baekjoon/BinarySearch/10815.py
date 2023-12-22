# 작성일자: 2023-12-21 THU, 작성자: AN밤비
# 10815번 숫자 카드
# 슈도코드

# 함수 이진탐색(cards, target):
#     시작인덱스 = 0
#     끝인덱스 = cards의 길이 - 1

#     동안 시작인덱스가 끝인덱스보다 작거나 같으면:
#         중간인덱스 = (시작인덱스 + 끝인덱스) // 2
#         만약 cards[중간인덱스] == target이면:
#             TRUE 반환
#         그렇지 않으면 만약 cards[중간인덱스] < target이면:
#             시작인덱스 = 중간인덱스 + 1
#         그렇지 않으면:
#             끝인덱스 = 중간인덱스 - 1

#     FALSE 반환

# 함수 해결():
#     내카드개수
#     내카드리스트
#     내카드리스트를 정렬

#     확인카드개수
#     확인카드리스트

#     각각의 확인할 카드에 대해서 반복:
#         만약 이진탐색(내카드리스트, 확인카드)이면:
#             출력 1
#         그렇지 않으면:
#             출력 0

# 만약 __name__ == "__main__"이면:
#     해결()


def binarySearch(myCardList, cardCheckList):
    startIndex, endIndex = 0, len(myCardList) - 1

    while startIndex <= endIndex:
        mid = (startIndex + endIndex) // 2
        if myCardList[mid] == cardCheckList:
            return True
        elif myCardList[mid] < cardCheckList:
            startIndex = mid + 1
        else:
            endIndex = mid - 1
    return False


def solution():
    myCardCount = int(input())
    myCardList = list(map(int, input().split()))
    myCardList.sort()

    cardCheckCount = int(input())
    cardCheckList = list(map(int, input().split()))

    # 각각의 확인할 카드에 대해 이진 탐색 수행 및 결과 출력
    for card in cardCheckList:
        if binarySearch(myCardList, card):
            print(1, end=" ")
        else:
            print(0, end=" ")


if __name__ == "__main__":
    solution()
