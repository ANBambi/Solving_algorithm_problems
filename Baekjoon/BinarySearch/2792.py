# 작성일자: 2023-12-22 FRI, 작성자: AN밤비
# 2792번 보석 상자
# 슈도코드

# 주어진 상자 크기로 모든 보석수를 나눌 수 있는지 확인하기
# 함수 isPossible(크기, 보석수, 학생수):
#     count초기화
#     보석수만큼 반복 :
#         count에 (보석수 / 크기) 추가하기

#     count가 아이들 수보다 크거나 같을 경우 반환

# 함수 binarySearch(보석들, 받는 애들 수):
#     시작점, 끝점 = 1, 보석수 최댓값

#     결과 초기화
#     while 시작점 <= 끝점:
#         mid = (시작점 + 끝점) // 2

#         만약 isPossible(중간값, 보석수, 학생수):
#             결과에 중간값 넣기
#             시작점 = 중간값 + 1
#         아니면:
#             끝점 = 중간값 - 1
#     결과 반환

# 함수 main():
#     children(아이들 수), jewelCount(보석갯수)
#     보석수 = [보석갯수만큼 for문으로 입력받기 _ ]

#     답 = binarySearch함수에 보석수, 받는 애들 수 :
#         답 출력

# Python 스크립트가 직접 실행될 때 해당 블록코드 실행하기

import sys


def isPossible(size, jewels, childrens):
    count = 0
    for jewel in jewels:
        count += (jewel + size - 1) // size
        # isPossible 함수, 올림을 위해 (jewel + size - 1) // size 함

    return count <= childrens


def binarySearch(jewels, childrens):
    start, end = 1, max(jewels)

    result = 0
    while start <= end:
        mid = (start + end) // 2

        if isPossible(mid, jewels, childrens):
            result = mid
            end = mid - 1
        else:
            start = mid + 1

    return result


def main():
    childrens, jewelCount = map(int, sys.stdin.readline().split())
    jewels = [int(sys.stdin.readline()) for _ in range(jewelCount)]

    answer = binarySearch(jewels, childrens)

    print(answer)


if __name__ == "__main__":
    main()
